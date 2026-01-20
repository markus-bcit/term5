The Quiet Work: Establishing Control
User and Access Control Lab Introduction

D’Arcy Smith

January 5th, 2026
The Quiet Work: Establishing Control
© 2025–2026 D’Arcy Smith. All rights reserved.

No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any
form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without
prior written permission of the author, except for brief quotations used for review or scholarly
citation.

This work is part of The Quiet Work series.

First edition — January 2026

The information in this book is provided for educational purposes only. The author assumes no
responsibility for the misuse of the material contained herein.
Morgan closes the report and sets it aside, leaving the conference table bare except for Pat’s
notebook and Jordan’s pen.

“Everything we’ve talked about so far,” Morgan says, “has been conceptual. Users, groups,
permissions. Now we need to make sure that the model actually matches what the system
does.”

Pat looks up. “So this is where people usually get confident too early.”

“Yes,” Morgan says. “This is where assumptions quietly replace verification.”

Jordan shifts in their chair. “Permissions always look obvious. Until you test them.”

Morgan nods once. “Exactly. Linux permissions are not intentions. They’re claims. The only way
to know if a claim is true is to try to cross the boundary.”

Morgan walks to the whiteboard and writes a single word:

       VERIFY

“Today isn’t about memorizing chmod values,” Morgan says. “If you leave remembering octal
numbers, you missed the point. This work is about proving that you understand what a
permission means.”

Pat flips to a clean page. “So we’re treating permissions like statements.”

“Yes,” Morgan says. “Statements about who can do what. And like any statement, they can be
wrong.”

Morgan draws a simple diagram: a user icon, a group label, and a file.

“When someone says, ‘the group has read access,’ what they’re really saying is: any account in
this group can read this asset. That’s a claim. The kernel will either agree or disagree.”

Jordan taps the pen against the notebook. “And the only honest way to check is to become that
user.”

“Right,” Morgan says. “Not in your head. Not by reading ls output and assuming. You switch
identities and attempt the action.”

Morgan underlines VERIFY.
“In this exploration,” Morgan continues, “you will create identities that mean nothing. Test users.
Test groups. Files that don’t matter. That’s intentional. It lets you focus on the access decision
without fear of breaking something important.”

Pat nods. “So the system becomes a controlled experiment.”

“Yes,” Morgan says. “And like any experiment, cleanup matters. When you’re done, there
should be no trace that you were here except your understanding.”

Jordan glances at the whiteboard. “What about directories? People always trip there.”

Morgan smiles slightly. “Good. You’re supposed to. Directories expose where mental models
are fuzzy.”

Morgan adds two more words beneath VERIFY:

       ENTER
       LIST

“These are not the same action,” Morgan says. “Linux does not treat them as the same action. If
you believe they are, the lab will correct you.”

Pat lets out a quiet breath. “So we’re going to hit at least one surprise.”

“If you don’t,” Morgan says, “you weren’t honest enough in your testing.”

Morgan steps back from the board. “Everything you do in this exploration follows the same
pattern. Decide what access you intend. Set permissions to express that decision. Test it as
another user. Then translate the result into plain language.”

Jordan looks up. “And if the sentence is hard to write…”

“... then your understanding isn’t finished,” Morgan says. “Go back and test again.”

Morgan gathers the remaining markers and sets them down neatly. “By the end, you should be
able to look at any file or directory and say, without hesitation, who can reach it and what they
can do from there.”

Pat closes the notebook. “And that’s the same skill we need for the findings.”

“Exactly,” Morgan says. “This exploration is small on purpose. But the thinking scales.
Production systems are just larger collections of the same decisions.””
Morgan pauses at the door. “Remember: permissions don’t fail silently. People do, when they
stop checking.”

The door closes softly behind them, leaving the room quiet and ready for work.
