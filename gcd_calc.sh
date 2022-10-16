#!/usr/bin/bash

# The program calculates the greatest common divisor (GCD) of 2 numbers. 

echo "Welcome to the GCD calculator program."
gcd () # takes 2 args
{
  echo "To quit press ENTER without entering any data."
  read -p "Enter 2 numerals as <integer> <integer>: " a b
  initial_a=$a
  initial_b=$b
  if [[ -z $a && -z $b ]]
  then
    echo "You didn't enter any data to process. Exiting program..."
    echo "Exited. Bye!"
    exit
  elif [[ -z $b || $a != ?(-)+([0-9]) || $b != ?(-)+([0-9]) ]]
  then
    echo "You entered wrong data type or not enough numerals. Note: only integers can be operated!"
    gcd $a $b
  elif [[ $a -eq 0 || $b -eq 0 ]]
  then
    echo "0 cannot be operated for the GCD!"
    gcd $a $b
  else
    while [[ $a -ne $b ]]
    do
      if [[ $a -gt $b ]]
      then
        let "a -= $b"
      else
        let "b -= $a"
      fi
    done
    echo "The GDC of $initial_a and $initial_b is $a."
    while [[ true ]]
    do
      gcd $a $b
    done
  fi
}

gcd $a $b

