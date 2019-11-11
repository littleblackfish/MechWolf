from ..stdlib.active_component import ActiveComponent


class MotorHatMotor(ActiveComponent):
    """
    DC motor connected to an Adafruit Motor HAT for Raspberry Pi

    See: https://www.adafruit.com/product/2348

    Arguments:
    - `motor_id`: Outputs number (M1-M4) that this motor is connected to.

    Attributes:
    - `throttle`: Number between 1 and -1 describing the speed of this motor

    """

    metadata = {
        "author": [
            {
                "first_name": "Murat",
                "last_name": "Ozturk",
                "email": "muzcuk@gmail.com",
                "institution": "Indiana University, School of Informatics, Computing and Engineering",
                "github_username": "littleblackfish",
            }
        ],
        "stability": "beta",
        "supported": True,
    }

    def __init__(self, motor_id, name=None ):
        super().__init__(name=name)

        self._motor_id = motor_id
        self.throttle=0.0

        self._base_state = dict(throttle=0.0)

    def __enter__(self):
        from adafruit_motorkit import MotorKit
        self._kit = MotorKit()

        if self._motor_id == 1 :
            self._motor = self._kit.motor1
        elif self._motor_id == 2 :
            self._motor = self._kit.motor2
        elif self._motor_id == 3 :
            self._motor = self._kit.motor3
        elif self._motor_id == 4 :
            self._motor = self._kit.motor4

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._motor.throttle=0.0
        del self._motor
        del self._kit

    async def _update(self):
        self._motor.throttle = self.throttle
