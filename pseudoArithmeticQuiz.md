
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
```
