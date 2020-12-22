# Metrics

We analyzed overall 41 metrics. All non-discriminatory complexity metrics (i.e., that show non-zero and different values for our snippets) are in `SnippetComplexityMetricsValues.csv`.

## Class Representatives

- Lines of Code (LOC)
- Halstead
- McCabe
- [DepDegree](https://www.sosy-lab.org/~dbeyer/DepDigger/)

## MetricsReloaded

We computed the following metrics with [MetricsReloaded](https://github.com/BasLeijdekkers/MetricsReloaded/):

- "ASSERT": "Calculates the total number of assert statements in each method."
- "B": "Calculates the Halstead Bugs metric for a method. The Halstead Bugs is intended as an estimate of the number of bugs in a method. In practice, it has usually been found to underestimate. "
- "BRANCH":"Calculates the total number of non-structured branch statements in each method. Non-structured branch statements include continue statements and branch statements outside of switch statements."
- "CALL": "Calculates the total number of method call expressions in each method."
- "CALLED": "Calculates the number places in the project at which each method may be called. This includes both calls to the method directly and calls to any method which it overrides."
- "CALLEDp": "Calculates the number places in the product code of the project at which each method may be called. This includes both calls to the method directly and calls to any method which it overrides."
- "CAST": "Calculates the number of typecast or instanceof expressions in each non-abstract method. Excessive use of typecasting may be a sign of an ill-structured program. "
- "CAUGHT":"Calculates the number of exception classes which are caught in each method."
- "CDENS":"Calculates the ratio of control statements to all statements for each method."
- "CLOC":"Calculates the number of lines of comments in each method. Whitespace is not counted for purposes of this metric."
- "COM_RAT":"Calculates the ratio of lines of comments to total lines of code in each method. Whitespace is not counted for purposes of this metric."
- "CONTROL": "Calculates the total number of control statements in each method. Control statements include if, for, while, do, try, break, continue, switch, and synchronized statements. "
- "D":"Calculates the Halstead Difficulty metric for a method. The Halstead Difficulty is intended to correspond to the level of difficulty of understanding a method. "
- "E":"Calculates the Halstead Effort metric for a method. The Halstead Effort is intended to correspond to the level of effort necessary to understand a method. "
- "ev(G)":"Calculates the essential complexity of each non-abstract method. Essential complexity is a graph-theoretic measure of just how ill-structured a method's control flow is. Essential complexity ranges from 1 to v(G), the cyclomatic complexity of the method. "
- "EXEC":"Calculates the total number of executable statements in each method. Executable statements are defined to be any non-control statement. "
- "EXP":"Calculates the total number of expressions in each method. "
- "IF_NEST":"Calculates the maximum depth of nesting of conditional (if) statements in each method. "
- "iv(G)":"Calculates the design complexity of a method. The design complexity is related to how interlinked a methods control flow is with calls to other methods. Design complexity ranges from 1 to v(G), the cyclomatic complexity of the method. Design complexity also represents the minimal number of tests necessary to exercise the integration of the method with the methods it calls. "
- "JLOG":"Calculates the number of lines of javadoc comments in each method. Whitespace is not counted for purposes of this metric."
- "LOC":"Calculates the number of lines of code in each method. Comments are counted for purposes of this metric, but whitespace is not."
- "LOOP":"Calculates the total number of loop statements in each method. For, while, and do-while loops are counted. "
- "LOOP_NEST":"Calculates the maximum depth of nesting of loop statements in each method. For, while, and do-while loops are counted. "
- "N":"Calculates the Halstead Length metric for a method. The Halstead length of a method is defined as the total number of operators and operands in a method. "
- "n":"Calculates the Halstead Vocabulary metric for a method. The Halstead Vocabulary of a method is defined as the total number of distinct operators and operands in a method. "
- "NBD":"Calculates the maximum nesting depth of each method: NEST"
- "NCLOC":"Calculates the number of non-comment lines of code in each method. Comment and empty lines are not counted by this metric. "
- "NP":"Calculates the number of parameters for each method. "
- "NTP":"Calculates the total number of type parameters of each method. "
- "NULL":"Calculates the number of comparisons with null in each method. "
- "QCP_CRCT":"Calculates the Quality Criteria Profile (Correctness) of a method. This is a synthetic metric, designed to estimate the difficulty of determining the correctness of given method. Lower scores are better. Quality Criteria Profile (Correctness) is defined as: QCP_CRCT = D + CONTROL + EXECUTABLE + (2*V(g)) "
- "QCP_MAINT":"Calculates the Quality Criteria Profile (Maintainability) of a method. This is a synthetic metric, designed to estimate the difficulty of maintenance for a given method. Lower scores are better. Quality Criteria Profile (Maintainability) is defined as: QCP_MAINT = (3*N) + EXEC + CONTROL + NEST + (2*V(g)) + BRANCH "
- "QCP_RLBTY":"Calculates the Quality Criteria Profile (Reliability) of a method. This is a synthetic metric, designed to estimate the reliability of given method. Lower scores are better. Quality Criteria Profile (Correctness) is defined as: QCP_RLBTY = N + (2*NEST) + (3*V(g)) + BRANCH + CONTROL + EXEC "
- "RETURN":"Calculates the total number of return points for each method. This includes any return statements as well as the implicit return at the end of constructors and methods returning void. "
- "RLOC":"Calculates ratio of lines of code for a method to the lines of code for it's containing class. Methods which have high relative lines of code values may indicate poor abstraction. "
- "STAT":"Calculates the total number of statements in each method. "
- "TCOM_RAT":"Calculates the ratio of lines of comments to total lines of source code in each method. Whitespace is not counted for purposes of this metric. "
- "THROWS":"Calculates the number of exception classes each method declares in its \"throws\" clause.",
- "TODO":"Calculates the number of TODO comments in each method. The format of TODO comments is defined in the Settings | Editor | TODO configuration panel. "
- "V":"Calculates the Halstead Volume metric for a method. The Halstead Volume is intended to correspond to the size of a method, and is defined as N * log(n), where N is the Halstead Length metric for the method and n is the Halstead Vocabulary metric. "
- "v(G)":"Calculates the cyclomatic complexity of each non-abstract method. Cyclomatic complexity is a measure of the number of distinct execution paths through each method. This can also be considered as the minimal number of tests necessary to completely exercise a method's control flow. In practice, this is 1 + the number of if's, while's, for's, do's, switch cases, catches, conditional expressions, &&'s and ||'s in the method."

## SonarQube

We used SonarQube to compute their cognitive complexity metric:

- [Cognitive Complexity](https://next.sonarqube.com/sonarqube/)
