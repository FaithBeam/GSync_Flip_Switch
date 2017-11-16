# GSync Flip Switch
Switches whichever mode your GSync monitor is in. If GSync is on, it is turned off. If GSync is off, it is turned on.

[![GSync Flip Switch Youtube Video](https://i.imgur.com/QuKjhE1.jpg)](https://www.youtube.com/watch?v=1w7AlD-x3vs "GSync Flip Switch Example Youtube Video")

## Requirements
* Linux kernel from the past 10 years
* Python >= 3.5 (And also in your path)
* Nvidia Driver >= 387.12
* nvidia-settings
* GSync Monitor

## Usage
Just run the .py file.

## Gotchas
* Running the tool back-to-back too quickly may cause settings to not be applied.
* Untested in multi-monitor setups.

## Why Disable GSync?
Many monitors that support GSync also support some sort of low motion blur mode (ULMB, LightBoost, DyAc, ELMB). GSync must be disabled to use these modes. Read more here: https://www.blurbusters.com/faq/motion-blur-reduction/

Not responsible for sudden death of monitor or any damage this may cause.
