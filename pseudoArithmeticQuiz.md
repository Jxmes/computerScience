*Pseudocode for arithmeticQuiz.py*

```
START

INPUT name;
WHILE name IS empty:
  INPUT name;

OUTPUT welcome message with name;

WHILE counter < 10:
    generate numberOne;
    generate numberTwo;
    generate operator;

    OUTPUT question(numberOne, operator, numberTwo);
    add 1 to counter;
    INPUT answer;

    IF answer IS == question:
      add 1 to score;
      OUTPUT congratulations message;
    ELSE:
      OUTPUT unlucky message;

OUTPUT congratulations message with total score;
IF score IS <= 5:
  OUTPUT try harder next time message;
ELIF score IS < 7:
  OUTPUT almost there message;
ELSE:
  OUTPUT well done message;

END
```
