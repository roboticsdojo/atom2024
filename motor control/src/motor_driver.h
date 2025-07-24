/***************************************************************
   Motor driver function definitions - by James Nugen
   *************************************************************/

#ifdef L298_MOTOR_DRIVER
  #define RIGHT_MOTOR_ENABLE 11
  #define RIGHT_MOTOR_FORWARD  9
  #define RIGHT_MOTOR_BACKWARD 10
  #define LEFT_MOTOR_ENABLE 6
  #define LEFT_MOTOR_FORWARD   7
  #define LEFT_MOTOR_BACKWARD  8
  
#endif

void initMotorController();
void setMotorSpeed(int i, int spd);
void setMotorSpeeds(int leftSpeed, int rightSpeed);
