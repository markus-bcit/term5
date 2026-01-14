Features,
Scenarios and
Stories
Fatemeh Riahi
Based on Ian Sommerville
Overview

• Importance of features in product design
• How to make list of features by making personas, scenarios.
• In class group exercise!
Key component in product designs
       Business needs
                         Dissatisfaction
      that are not met
                          with existing
         by current
                            product
          product


                  Changes in
                 technologies
Software Features

• Fragments of functionality:
    • Print, change background, sing out
• Before anything, we need to create a list of features
• Feature list should be starting point of product design.
How to build feature list?

• User and customer understanding
  • User interviews, surveys, task analysis
  • Early and cheap release of our MVP
     • Informal user analysis and discussion
Feature Description
Feature Description Example
One way of representing users: Personas

• One way of understanding potential users
• Imagined user
• For example, all personas for a dentist appointment management system
  are: Dentists, receptionist and patients
Persona descriptions

• Paint a picture; short and easy to read
• Describe user background and product usage
• Educational background and technical skills
Driving persona

• Based on an understanding of potential product users, their jobs,
  background, etc.
• Survey the potential users
• Abstract the essential information about the different types of product
  users
• Sometimes there is limited user information, and we must come up with
  proto personas
Persona Descriptions
Personal Example

• Elena, a school IT technician
  Elena, age 28, is a senior IT technician in a large secondary school (high school) in Glasgow
  with over 2000 students. She has a diploma in electronics from Potsdam University. She
  hopes to develop her career in Scotland. She was originally appointed as a junior
  technician but was promoted, in 2014, to a senior post responsible for all the school
  computers.


• Although not involved directly in teaching, Elena is often called on to help in computer
  science classes. She is a competent Python programmer and is a ‘power user’ of digital
  technologies. She has a long-term career goal of becoming a technical expert in digital
  learning technologies and being involved in their development. She wants to become an
  expert in the iLearn system and sees it as an experimental platform for supporting new
  uses for digital learning.
Benefits of Persona

• Help developers
   • Empathize with potential users
   • Step into users’ shoes
• Make sure that developers aren’t working on useless features
• Avoid unwarranted assumptions
Scenarios

• A scenario is a narrative that describes how a user, or a group of users,
  might use your system.
• There is no need to include everything in a scenario – the scenario isn’t a
  system specification.
• It is simply a description of a situation where a user is using your product’s
  features to do something that they want to do.
• Scenario descriptions may vary in length from two to three paragraphs up
  to a page of text.
Using ilearn: Learning management system
for class project

• Fishing in Ullapool
  Jack is a primary school teacher in Ullapool. He has decided that a class project should be focused around the fishing
  industry in the area
• As part of this, students are asked to collect old photographs related to fishing and fishing communities in the area.
  They use an iLearn wiki to gather together fishing stories and SCRAN (a history archive site) to access newspaper
  archives and photographs. However, Jack also needs a photo-sharing site as he wants students to take and comment
  on each others’ photos and to upload scans of old photographs that they may have in their families. He needs to be
  able to moderate posts with photos before they are shared, because pre-teen children can’t understand copyright
  and privacy issues.


• Jack sends an email to a primary school teachers’ group to see if anyone can recommend an appropriate system.
  Two teachers reply and both suggest that he uses KidsTakePics, a photo-sharing site that allows teachers to check
  and moderate content. As KidsTakePics is not integrated with the iLearn authentication service, he sets up a teacher
  and a class account with KidsTakePics.
• He uses the the iLearn setup service to add KidsTakePics to the services seen by the students in his class so that,
  when they log in, they can immediately use the system to upload photos from their phones and class computers.
Elements of Scenario description
Writing Scenarios

• User centric
• Avoid Technical Details
• Comprehensive coverage
User involvement strategies and
challenges

• Strategies
  • Initial Scenario Creation
  • User Feedback and Iteration
  • Refinement and Expansion
• Challenges:
  • User generated content: too detailed. No abstraction.
     • How to mitigate this?
        • Guidance and facilitation
User Stories

• Definition: User stories are more specific than scenarios.
• Content: Each user story focuses on a single functionality or need,
• Standard Format of a User Story:
    • As a [role], I [want | need] to [do something].
• Extended Format with Justification:
    • As a [role], I [want | need] to [do something] so that [reason].
                  • Product backlog as user stories
User stories in   • Focus on implementable unit
planning          • Managing complex feature
Example: System backup and restoration

• Epic:
    • As a system manager, I need a way to backup the system and restore
      either individual applications, files, directories, or the whole system.
• Stories:
    • As a system manager, I want to backup individual files, so that I can easily
      restore them if they are lost or corrupted.
    • As a system manager, I want to restore individual applications quickly,
      ensuring minimal downtime in case of application failure.
    • As a system manager, I need the ability to perform full system backups
      weekly, to ensure comprehensive data protection.
User stories describing the group
             feature
Feature Derivation

• Features can be identified directly from the product vision or from
  scenarios.
• You can highlight phrases in Scenario
    • You should think about the features needed to support user actions,
      identified by active verbs, such as use and choose.
Product Vision

• Product Vision Statement (Using Moore’s Template):
   • For university students and faculty - who need a flexible and interactive
     platform to manage coursework and enhance learning experiences -
     the AcademiaHub is a web-based learning management system - that
     offers personalized learning paths and real-time collaboration tools -
     unlike traditional one-size-fits-all educational platforms - our product
     tailors learning experiences to personalized and individual academic
     needs and fosters active learning through collaboration.
Derived Features from Product Vision

• Personalized Learning Paths: Allows users to create and follow
  customized learning journeys based on their academic goals and
  interests.
• Real-Time Collaboration Tools: Provides features like shared
  whiteboards, real-time document editing, and video conferencing to
  support interactive learning.
• Adaptive Learning Analytics: Integrates machine learning to analyze
  student performance and adjust content delivery to optimize learning
  outcomes.
Scenario

• Scenario: Professor Smith wants to use an online platform to coordinate a
  semester-long project involving multiple groups of students, tracking their
  progress, scheduling milestones, and providing targeted feedback based on
  individual and group performance.
Derived Features from Scenario

• Group Management Interface: Tools for creating student groups,
  assigning roles, and managing memberships.
• Project Tracking Dashboard: A comprehensive dashboard that allows
  tracking of project milestones, submission deadlines, and overall progress
  for each group.
• Feedback System: Features enabling Professor Smith to provide
  individualized feedback and grade submissions, with support for audio
  and text comments.
Feature List

• The output of the feature identification process should be a list of features
  that you use for designing and implementing your product.
• There is no need to go into a lot of detail about the features at this stage.
  You add detail when you are implementing the feature.
• You can describe features using a standard input-action-output template
  by using structured narrative descriptions or by a set of user stories.
Authentication Feature example
Feature Example: Group Management
Interface

• Description:
   • The Group Management Interface allows instructors to create, modify,
     and manage student groups within online courses. This feature
     includes tools for assigning roles, setting permissions, and tracking
     group membership changes over time. It aims to facilitate seamless
     collaboration among students by organizing them into structured
     groups, which can be tailored to various project types and class
     activities.
Feature Example: Group Management
Interface

• Constraints:
   • User Roles: Only users identified as "Instructors" or "Teaching Assistants"
     have the authority to create and manage groups. Students can view group
     memberships but cannot alter them.
   • Scalability: The interface must efficiently handle classes of varying sizes, from
     small seminars to large lectures with hundreds of students, without
     performance issues.
   • Integration: This feature must integrate smoothly with other platform
     components like the Project Tracking Dashboard and Real-Time Collaboration
     Tools without disrupting existing functionalities.
   • Data Privacy: Must comply with educational data privacy regulations (e.g.,
     FERPA in the U.S.) to protect student information.
Innovation and feature identification

• Scenarios and user stories should always be your starting point for identifying
  product features.
    • Scenarios tell you how users work at the moment. They don’t show how they
      might change their way of working if they had the right software to support
      them.
    • Stories and scenarios are ‘tools for thinking’ and they help you gain an
      understanding of how your software might be used. You can identify a
      feature set from stories and scenarios.
• User research, on its own, rarely helps you innovate and invent new ways of
  working.
• You should also think creatively about alternative or additional features that help
  users to work more efficiently or to do things differently.
From personas, to Scenarios, Features
and Stories
Takeaways!

• A software product feature is a fragment of functionality that implements
  something that a user may need or want when using the product.
• The first stage of product development is to identify the list of product features in
  which you identify each feature and give a brief description of its functionality.
• Personas are ‘imagined users’ where you create a character portrait of a type of
  user that you think might use your product.
• A persona description should ‘paint a picture’ of a typical product user. It should
  describe their educational background, technology experience and why they
  might want to use your product.
• A scenario is a narrative that describes a situation where a user is accessing
  product features to do something that they want to do.
Takeaways!

• Scenarios should always be written from the user’s perspective and should be
  based on identified personas or real users.
• User stories are finer-grain narratives that set out, in a structured way, something
  that a user wants from a software system.
• User stories may be used as a way of extending and adding detail to a scenario or
  as part of the description of system features.
• The key influences in feature identification and design are user research, domain
  knowledge, product knowledge, and technology knowledge.
• You can identify features from scenarios and stories by highlighting user actions
  in these narratives and thinking about the features that you need to support
  these actions.
More Examples
Emma’s Scenario
• Emma’s scenario is different from Jack’s scenario in that it
  describes a common and well-understood process rather
  than something new.
• Emma is an e-learning sceptic, and she is not interested in
  innovative applications. She wants a system that will make
  her life easier and reduce the amount of routine
  administration that she has to do.
• The scenario discusses how parts of the process (setting up
  an email group and web page) are automated by the iLearn
  system.
Emma’s scenario: Using iLearn for
administration
• She names the group and confirms that it should be created. The app sets up an icon on her iLearn
  screen to represent the group, creates an email alias for the group and asks Emma if she wishes to
  share the group. She shares access with everyone in the group, which means that they also see the
  icon on their screen. To avoid getting too many emails from students, restricts sharing of the email
  alias to Jamie and Claire.


• The group management app then asksEmma if she wishes to set up a group web page, wiki and
  blog. Emma confirms that a web page should be created and she types some text to be included on
  that page.


• She then accesses flickr using the icon on her screen, logs in and creates a private group to share
  trip photos that students and teachers have taken. She uploads some of her own photos from
  previous trips and emails an invitation to join the photo-sharing group to the Battlefield email list.
  Emma uploads material from her own laptop that she has written about the trip to iLearn and
  shares this with the ‘Battlefields Group’. This action adds her documents to the web page and
  generates an alert to group members that new material is available.
Emma’s scenario: Using iLearn for
administration
• Emma is teaching the history of the First World War to a class of 14 year olds (S3). A group of S3
  students are visiting the historic World War One battlefields in northern France. She want to set up
  a ‘battlefields group’ where the students who are attending the trip can share their research about
  the places they are visiting as well as their pictures and thoughts about the visit.


• From home, she logs onto the iLearn system system using her Google account credentials. Emma
  has two iLearn accounts – her teacher account and a parent account associated with the local
  primary school. The system recognises that she is a multiple account owner and asks her to select
  the account to be used. She chooses the teacher account and the system generates her personal
  welcome screen. As well as her selected applications, this also shows management apps that help
  teachers create and manage student groups.


• Emma selects the ‘group management’ app, which recognizes her role and school from her identity
  information and creates a new group. The system prompts for the class year (S3) and subject
  (history) and automatically populates the new group with all S3 students who are studying history.
  She selects those students going on the trip and adds her teacher colleagues, Jamie and Claire, to
  the group.
        Figure 3.6 User stories from Emma’s scenario




Features, Scenarios and Stories                        © Ian Sommerville 2018:   4
                                                                                 0
