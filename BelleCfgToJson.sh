#!/usr/bin/env bash
python ConfParser_last.py
if [ $? -eq 0 ]
  then python comment_deleter.py
    if [ $? -eq 0 ]
      then python BelleConfDecoder.py
        if [ $? -eq 0 ]
          then python JsonToRucio.py
              if [ $? -eq 0 ]
                then echo "sucessful excecution"
              else
                echo "fourth script fail: JsonToRucio.py"
              fi
        else
          echo "third script fail: BelleConfDecoder.py"
        fi
    else
      echo "second script fail: comment_deleter.py"
    fi
else
  echo "fist script fail: ConfParser_last.py"
fi
