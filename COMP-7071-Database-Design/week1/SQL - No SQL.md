Intro to Relational Model


   SQL Vs NoSQL Databases
                                  Outline

§   Structure of Relational Databases
§   Database Schema
§   Keys
§   Schema Diagrams
§   Relational Query Languages
§   The Relational Algebra
Example of a Instructor Relation

                               attributes
                             (or columns)



                               tuples
                             (or rows)
                                 Attributes

§ The set of allowed values for each attribute is called the domain of the
   attribute
§ Attribute values are (normally) required to be atomic; that is, indivisible
§ The special value null is a member of every domain. Indicated that the
   value is “unknown”
§ The null value causes complications in the definition of many operations
                    Relations are Unordered

§ Order of tuples is irrelevant (tuples may be stored in an arbitrary order)
§ Example: instructor relation with unordered tuples
                            Database Schema

§ Database schema -- is the logical structure of the database.
§ Database instance -- is a snapshot of the data in the database at a
   given instant in time.
§ Example:
   • schema: instructor (ID, name, dept_name, salary)
   • Instance:
                                   Keys

§ One of the candidate keys is selected to be the primary key.
§ Foreign key constraint: Value in one relation must appear in another
   • Referencing relation
   • Referenced relation
   • Example: dept_name in instructor is a foreign key from instructor
       referencing department
Schema Diagram for University Database
                               Union Operation

§ The union operation allows us to combine two relations
§ Notation: r È s
§ For r È s to be valid.
   1. r, s must have the same arity (same number of attributes)
   2. The attribute domains must be compatible (example: 2nd
       column of r deals with the same type of values as does the
       2nd column of s)
§ Example: to find all courses taught in the Fall 2017 semester, or in the
   Spring 2018 semester, or in both
     Õcourse_id (s semester=“Fall” Λ year=2017 (section)) È
     Õcourse_id (s semester=“Spring” Λ year=2018 (section))
section table
                       Union Operation (Cont.)

§ Result of:
     Õcourse_id (s semester=“Fall” Λ year=2017 (section)) È
     Õcourse_id (s semester=“Spring” Λ year=2018 (section))




               È                                    =
                   Set-Intersection Operation

§ The set-intersection operation allows us to find tuples that are in both
   the input relations.
§ Notation: r Ç s
§ Assume:
   • r, s have the same arity
   • attributes of r and s are compatible
§ Example: Find the set of all courses taught in both the Fall 2017 and the
   Spring 2018 semesters.
      Õcourse_id (s semester=“Fall” Λ year=2017 (section)) Ç
      Õcourse_id (s semester=“Spring” Λ year=2018 (section))

    • Result
                            Types of Data
§ Data can be broadly classified into four types:
  1. Structured Data:
     §   Have a predefined model, which organizes data into a form that is
         relatively easy to store, process, retrieve
         and manage
     §   E.g., relational data



  2. Unstructured Data:
     §   Opposite of structured data
     §   E.g., Flat binary files containing text, video or audio
     §   Note: data is not completely devoid of a structure (e.g., an audio file may
         still have an encoding structure and some metadata associated with it)
                           Types of Data
§ Data can be broadly classified into four types:
  3. Dynamic Data:
     §   Data that changes relatively frequently
     §   E.g., office documents and transactional entries in a financial database



  4. Static Data:
     §   Opposite of dynamic data
     §   E.g., Medical imaging data from MRI or CT scans
                                        Why Classifying Data?
§ Segmenting data into one of the following 4 quadrants can
  help in designing and developing a pertaining storage
  solution                             Static
                                          Dynamic
          Structured Unstructured




                                    Media Production, eCAD,     Media Archive, Broadcast,
                                      mCAD, Office Docs             Medical Imaging



                                    Transaction Systems, ERP,     BI, Data Warehousing
                                              CRM




§ Relational databases are usually used for structured data

§ File systems or NoSQL databases can be used for (static),
  unstructured data (more on these later)
             Scaling Traditional Databases
§ Traditional RDBMSs can be either scaled:
  § Vertically (or Up)
     §   Can be achieved by hardware upgrades (e.g., faster CPU, more memory,
         or larger disk)
     §   Limited by the amount of CPU, RAM and disk that can be configured on a
         single machine


  § Horizontally (or Out)
     §   Can be achieved by adding more machines
     §   Requires database sharding and probably replication
     §   Limited by the Read-to-Write ratio and communication overhead
                            Why Sharding Data?
§ Data is typically sharded (or striped) to allow for
  concurrent/parallel accesses

                               Input data: A large file


        Machine 1                    Machine 2               Machine 3
     Chunk1 of input data         Chunk3 of input data    Chunk5 of input data

     Chunk2 of input data         Chunk4 of input data    Chunk5 of input data




     E.g., Chunks 1, 3 and 5 can be accessed in parallel
               Amdahl’s Law: An Example


§ Suppose that:
   § 80% of your program can be parallelized
   § 4 machines are used to run your parallel version of
        the program

§ The speedup you can get according to Amdahl’s law
  is:


 Although you use 4 processors you cannot get a speedup
                  more than 2.5 times!
                                                      18
                                Real Vs. Actual Cases
    § Amdahl’s argument is too simplified


    § In reality, communication overhead and potential
          workload imbalance                            exist       upon         running             parallel
   Serial programs
            20      80                                                   20               80
                                                               Serial


 Parallel    20     20                                       Parallel    20     20
Process 1                                                   Process 1


Process 2                                                   Process 2

                                                                                                     Cannot be parallelized
Process 3                                                   Process 3
                                   Cannot be parallelized                                            Can be parallelized

Process 4                                                   Process 4                            Communication overhead
                                  Can be parallelized
                                                                                               Load Unbalance
            1. Parallel Speed-up: An Ideal Case                         2. Parallel Speed-up: An Actual Case
                       Some Guidelines

§ Here are some guidelines to effectively
                      benefit
 from parallelization:
  1.   Maximize the fraction of your program that can be parallelized


  2.   Balance the workload of parallel processes


  3.   Minimize the time spent for communication




                                                                        20
                  Why Replicating Data?
§ Replicating data across servers helps in:
  § Avoiding performance bottlenecks
  § Avoiding single point of failures
  § And, hence, enhancing scalability and availability
        Main Server




                        Replicated Servers
                  The Two-Phase Commit Protocol
   § The two-phase commit protocol (2PC) can be
      used to ensure atomicity and consistency
Phase I: Voting
                   VOTE_REQUEST
                   VOTE_COMMIT
                                  Participant 1   Database Server 1


                   VOTE_REQUEST

                   VOTE_COMMIT

    Coordinator                   Participant 2   Database Server 2

                   VOTE_COMMIT
                   VOTE_REQUEST


                                  Participant 3   Database Server 3
                  The Two-Phase Commit Protocol
  § The two-phase commit protocol (2PC) can be
      used to ensure atomicity and consistency
Phase II: Commit
                   GLOBAL_COMMIT               LOCAL_COMMIT


                               Participant 1                  Database Server 1


                   GLOBAL_COMMIT               LOCAL_COMMIT



    Coordinator                Participant 2                  Database Server 2



                   GLOBAL_COMMIT               LOCAL_COMMIT

   “Strict” consistency,
  which limits scalability!    Participant 3                  Database Server 3
                    The CAP Theorem
§ The limitations of distributed databases can be
  described in the so called the CAP theorem
   § Consistency: every node always sees the same data at
      any given instance (i.e., strict consistency)


   § Availability: the system continues to operate, even if
      nodes in a cluster crash, or some hardware or software
      parts are down due to upgrades


   § Partition Tolerance: the system continues to operate in
 CAP the presence
     theorem:        of network
              any distributed     partitions
                              database with shared data, can have at
        most two of the three desirable properties, C, A or P
                 The BASE Properties
§ The CAP theorem proves that it is impossible to guarantee
  strict Consistency and Availability while being able to
  tolerate network partitions


§ This resulted in databases with relaxed ACID guarantees

§ In particular, such databases apply the BASE properties:
   § Basically Available: the system guarantees Availability
   § Soft-State: the state of the system may change over time
   § Eventual Consistency: the system will eventually
     become consistent
                     NoSQL Databases
§ To this end, a new class of databases emerged,
  which mainly follow the BASE properties
  § These were dubbed as NoSQL databases
  § E.g., Amazon’s Dynamo and Google’s Bigtable


§ Main characteristics of NoSQL databases include:
  § No strict schema requirements
  § No strict adherence to ACID properties
  § Consistency is traded in favor of Availability
           Types of NoSQL Databases
§ Here is a limited taxonomy of NoSQL databases:

               NoSQL Databases



Document      Graph       Key-Value
 Stores      Databases     Stores
                   Document Stores
§ Documents are stored in some standard format or
  encoding (e.g., XML, JSON, PDF or Office
  Documents)
   § These are typically referred to as Binary Large Objects
    (BLOBs)


§ Documents can be indexed
  § This allows document stores to outperform traditional
    file systems


§ E.g., MongoDB and CouchDB (both can be queried
  using MapReduce)
           Types of NoSQL Databases
§ Here is a limited taxonomy of NoSQL databases:

               NoSQL Databases



Document      Graph       Key-Value
 Stores      Databases     Stores
                         Graph Databases
§ Data are represented as vertices and edges

                             00      s                           Id: 2
                         Id:1 l: know 0/03
                              e        1
                          Lab : 2001/                          Name: Bob
                                e
                           Sinc                                 Age: 22

                                      01        s                   r
                                  Id:1 l: know 0/03               be 4
                Id: 1
                                        e
                                   Lab : 2001/
                                                   1           em 2/1
                                          e                 _m   /0
               Name:                Sinc           105 l: is 011                   er
                                                                                      s
                                                 :                                b
                Alice              Id:1
                                       0       Id abe e: 2                      m
                                  Lab 3           L inc                    04 Me
               Age: 18                el: M                             :1 l:
                                            emb S                     Id abe
                                                ers                      L

                                                    Id: 3
                   Id:1                            Name:
                  Lab 02                           Chess
                 Sin el: is_                       Type:
                    ce:     m
                        200 embe                   Group
                            5/0     r
                               7/0
§ Graph databases are powerful for graph-like queries (e.g., find
                                  1

  the shortest path between two elements)

§ E.g., Neo4j and VertexDB
           Types of NoSQL Databases
§ Here is a limited taxonomy of NoSQL databases:

               NoSQL Databases



Document      Graph       Key-Value
 Stores      Databases     Stores
                  Key-Value Stores
§ Keys are mapped to (possibly) more complex
  value (e.g., lists)

§ Keys can be stored in a hash table and can be
  distributed easily

§ Such stores typically support regular CRUD
  (create, read, update, and delete) operations
   § That is, no joins and aggregate functions

§ E.g., Amazon DynamoDB and Apache Cassandra
