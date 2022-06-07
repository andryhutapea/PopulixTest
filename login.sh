# !/bin/bash
echo "Input Username & Password "

# Receive 2 inputs: username & password
read -p 'Username: ' username
read -p 'Password: ' password

# Valid username & password: qa & engineer
if [[ $username == "qa"  && $password == "engineer" ]]
then
    # apabila username & password sesuai
  echo -e "\nLogin Success\n"
else
    # apabila username & password sesuai
  echo -e "\nLogin failed\n"
fi

echo "Thankyou"