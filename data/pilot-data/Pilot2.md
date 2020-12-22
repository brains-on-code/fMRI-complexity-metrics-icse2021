## Pilot 2

We used a Google Form to look at five snippets: isPalindrome, arrayAverage, mergeSort, yesNo, and sortFiveElements.

## Participants

6 participants (PhD students) filled in the survey. It took them between 10-15 minutes to review the 5 snippets, perform ranking, and fill out the answers.

Then we discussed their responses after submitting. We started with looking at different interpretations of complexity. For me, this was very interesting, as there were many different perspectives. Students offered one or more of these perspectives:

\* **Gestalt/Mapping/Top-down comprehension**: How easily can you extract the purpose and goal of each line segment. If each segment was recognizable to them and connected to a goal, then it was generally considered "easy" or "low complexity".

\* "**How else can I write this**"?: This perspective asked if the code was written the best way, or if there were other designs or implementations that could be simpler. This view seems to stem from assessing the "elegance" of the code.

\* **Verification**: Another perspective involved determining how difficult it would be to test out the correctness of the solution. In other words, how confident would they be in their understanding of the code doing what it claims to do.

\* **Mechanical**: This involved aspects such as operators and number of variables in the code.

 

We next reviewed the total ranking participants gave. We found that the six students consistently ranked "arrayAverage" and "yesNo" as the least complex. "isPalindrome" was considered in the middle, but one participant ranked it as the most complex. Finally, "mergeSort" and "sortFiveElements" were consistently considered very complex.

 

Finally, we reviewed what participants found complex about "isPalindrome", "mergeSort", and "sortFiveElements".

 

Most participants mentioned "double iteration" as the most complex aspect of isPalindrome. One later mentioned that they were concerned that isPalindrome was implemented in a more complex fashion than it should be, and that's why they ranked as most complex. There was an interesting discussion on why mergeSort and sortFiveElements were considered complex (or not). For some, they mentioned for sortFiveElements, from the mapping perspective, they could easily identify each line and determine it is performing a swap. So from that perspective, the method was actually very easy to understand and had low complexity. On the other hand, others mentioned that verification that the method actually performed a sort correctly was extremely difficult and would require considerable effort, and that's why they considered it most complex. Finally, for mergeSort, having comments, and recognizable "chunks" of the algorithm made it easier to understand, however, a lack of the domain knowledge about how the algorithm works exactly (and not having that information readily available) was cited as an additional reason for why the code could be considered complexity and difficult to understand. Finally, the last step perform the merge was considered complex from a mechanical point of view (many variables and operations).