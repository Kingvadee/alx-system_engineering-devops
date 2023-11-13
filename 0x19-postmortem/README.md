# AUTHOR:         DAVID OJEIFO[https://github.com/Kingvadee].
# COHORT:         13.
# Repo:           alx-system_engineering-devops.
# Directory:      0x19-postmortem. 

# Tasks :page_with_curl:


# For this project, we expect you to look at these concepts:
 * On-call
  * Being on-call
   (of a person) able to be contacted in order
   to provide a professional service if
   necessary, but not formally on duty.

#“our technicians are on call around the clock” :page_with_curl:
  * synonyms: on duty, on standby, available
    “Dr. Merton is on call this evening”

# Case-Study => Google :floppy_disk:
  * Users and consumers expect their favorite websites and services
    to be constantly accessible. Have you ever seen Facebook, Amazon,
    LinkedIn, Ebay down? Probably not. Any downtime means users
    frustration and potentially millions of dollars in loss. That’s
    true for the big players but also for any company where its online
    presence is crucial, which is the case for a lot of businesses.

  * This does not happen magically. Software engineers are building
    reliable systems that are supposed to be up and running 100% of the
    time, but sometimes things go sideways and the issue needs to be
    fixed as soon as possible. To achieve quick resolution time,
    companies are putting in place monitoring systems to detect any
    anomaly and alert the employee who is on-call. This sometimes
    happens during working hours, but also at 3am or at night.

# SETUP :page_with_curl:
	*  To be on call you need at least 4 components:
 * A service or website you want to monitor
 * A monitoring tool
 * An oncall management system
 * A software engineer (that’s you)
# C:\Users\user\OneDrive\Pictures\Screenshots\Screenshot 2023-11-12 190244.png

# A service or website you want to monitor :page_with_curl:
 * You can monitor thousands of things:
    * (i)	Is my website returning HTTP 200?
    * (ii)	Is my website loading in less than 500ms?
    * (iii)	Is my webserver daemon up?
    * (iv)	Is there more than 50% free disk space on my server?
    * ...
# A monitoring tool:
 * You need to configure one or multiple monitoring tool(s) to your on-call
   system, they are the ones that will actually detect any anomaly and report
   it to the on-call platform. Check out the Monitoring concept page for
   recommandations.
# A on-call management system:
 * A lot of home tools can be used for that, you can for example in Nagios define
   on-call periods and then hook this up to a 3rd party service that can send a
   text message for you. This is fine when you are alone on-call but become very
   complicated when you have a team. That’s what a company started in 2009 is doing
   in the Cloud: PagerDuty. It’s a service that allows you to define on-call teams,
   escalation policies and services integration.

# On-call management system flow :page_with_curl:
 * Let’s get a bit more into detail about the flow of an on-call management system
   such as PagerDuty. First of all you have to understand that PagerDuty is not
   monitoring your website, it acts as a gateway between your monitoring tools and
   the software engineers that are on-call. Its goal is to alert, as soon as possible,
   as reliably as possible and as efficiently as possible the person or team on-call.
   That’s a very hard duty because if PagerDuty goes down then many sites or services
   going down at the same time won’t be fixed because the alerts won’t reach the on-call
   persons.
 * Let’s get into a simple and typical workflow:
   * 1.	An incident has been detected by an external monitoring tool that notifies
        PagerDuty.
   * 2. PagerDuty creates an incident and assigns it to the on-call person, the alert is
        in a “triggered” mode.
   * 3. The on-call person gets notified and acknowledges the alert meaning that the software
        engineer is looking into the problem.
   * 4. If the engineer cannot solve the issue, she/he can escalate it (pass it on) to another
        co-worker. PagerDuty also allows automatic escalation in case the on-call person does
        not acknowledge the alert (which means that for some reason the on-call person is not
        available - no battery on the phone, not hearing the ringtone and all sorts of good
        stuff :-))
   * 5. A brilliant software engineer (most likely a Holberton School member) solves the issue
        and marks the incident as solved. Depending on the type of alert and service that notified
        PagerDuty, it can be auto-resolved.

 * On-call teams are usually rated on 2 metrics:
   * [1]	MTA (Medium Time to Acknowledgement): The time between an alert/incident is created
		and an on-call person acknowledged it (which means that he or she is working toward
		a solution).
   * [2]	MTR (Medium Time to Resolution): The time between an alert/incident being created
		and this same incident/alert being marked as solved.
 * You obviously want these mean times to be as low as possible. MTA basically tells how good
   engineers are at answering their phone. MTR basically tells how good engineers are at solving
   issues.


# C:\Users\user\OneDrive\Pictures\Screenshots\Screenshot 2023-11-12 191023.png

# PagerDuty :floppy_disk:
 * We made a partnership so that Holberton School students can utilize PagerDuty for free. For every
   student a team is created (team of one), we will also have teams for group projects later on.
 * Every PagerDuty team has an automatically created and linked: - Escalation policy - Services (which
   are monitoring tools, we can add more services upon demand to Holberton School staff)
 * We advise you to create accounts with the recommended monitoring tools and to connect them with
   PagerDuty using the pre-created services.
 * Also make sure to configure your profile to fill in your contact information and define the
   Notification Rules.

# Background Context:
 * Any software system will eventually fail, and that failure can come stem from a wide range of
   possible factors:
   * bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing
     is normal and failing is actually a great opportunity to learn and improve. Any great Software
     Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine,
     but failing twice because of the same issue is not.

 * A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the
   system will write a summary that has 2 main goals:
   * To provide the rest of the company’s employees easy access to information detailing the cause of the
     outage. Often outages can have a huge impact on a company, so managers and executives have to
     understand what happened and how it will impact their work.
   * And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to
     make sure it will be fixed.

# Resources :page_with_curl:
 * Incident Report, also referred to as a Postmortem[https://sysadmincasts.com/episodes/20-how-to-write-an-incident-report-postmortem]

 * The importance of an incident postmortem process[https://www.atlassian.com/incident-management/postmortem]

 * What is an Incident Postmortem?[https://www.pagerduty.com/resources/learn/incident-postmortem/]


 * At the end of this project, request a review for your postmortem from a peer before the project’s deadline.
   If no peers have been reviewed, you should request a review from a TA or staff member. 

# Using 0x17. Web stack debugging #3 issue, a postmortem. :floppy_disk:
 * Requirements:
  * Issue Summary (that is often what executives will read) must contain:
  * duration of the outage with start and end times (including timezone)
  * what was the impact (what service was down/slow? What were user experiencing?
    How many % of the users were affected?)
  * what was the root cause
  * Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences)
    must contain:

 * when was the issue detected
 * how was the issue detected (monitoring alert, an engineer noticed something,
   a customer complained…)
 * actions taken (what parts of the system were investigated, what were the
   assumption on the root cause of the issue)
 * misleading investigation/debugging paths that were taken
 * which team/individuals was the incident escalated to
 * how the incident was resolved
 * Root cause and resolution must contain:

 * explain in detail what was causing the issue
 * explain in detail how the issue was fixed
 * Corrective and preventative measures must contain:

 * what are the things that can be improved/fixed (broadly speaking)
 * a list of tasks to address the issue (be very specific, like a TODO, example:
   patch Nginx server, add monitoring on server memory…)
 * Be brief and straight to the point, between 400 to 600 words

 * While postmortem format can vary, stick to this one so that you can get
   properly reviewed by your peers.

Please, remember that these blogs must be written in English to further your 
technical ability in a variety of settings.

# MY BLOG POST :page_with_curl:

 | 'Blog Post Link'   |                                                                     |
 |--------------------|---------------------------------------------------------------------|
