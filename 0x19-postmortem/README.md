![image](https://github.com/Preshladyp/alx-system_engineering-devops/assets/111128701/154cdfbc-0681-44a4-b470-d57c696e5267)



Web Stack Outage

Date of the Web Stack Outage: October 12, 2023

Time of Incident: October 10, 2023, 10:30 (UTC)

The incident will end at 2:00 PM (UTC) on October 11, 2023.

About 25 hours in length.

Summary
On October 10, 2023, a massive outage in our web stack disrupted a number of services and our users on a large scale. Before full service was resumed, the situation lasted for around 25 hours. The objective of this postmortem is to offer a thorough examination of the occurrence, its underlying causes, and the efforts taken to avoid a repeat.

Calendar of Events
The event started with a significant increase in error rates and a drop in service availability across a variety of services on October 10, 2023 10:30 AM (UTC).
The on-call crew was informed at 10:45 AM (UTC), and they started working right away.

11:30 AM (UTC): Initial investigation revealed that the database servers were experiencing high CPU and memory usage.
12:00 PM (UTC): The decision was made to restart the affected database servers to alleviate the performance issues. This action resulted in a brief service interruption.
1:30 PM (UTC): The database servers appeared stable after the restart, but the issue resurfaced within an hour.
4:00 PM (UTC): As error rates continued to rise, a decision was made to roll back a recent application update in an attempt to resolve the issue. This resulted in another brief service interruption.
October 11, 2023
1:00 AM (UTC): Despite the rollback, error rates remained high, and the database servers were still under heavy load.
8:30 AM (UTC): A deep-dive investigation identified a slow query that was repeatedly being executed and putting undue stress on the database.
10:00 AM (UTC): The slow query was optimized and tested, resulting in improved database performance.
12:00 PM (UTC): Service availability and error rates began to stabilize.
2:00 PM (UTC): The incident was declared resolved, and normal service operations were restored.
Root Causes
Unoptimized Query: The primary root cause of the outage was an unoptimized database query. This query, which was introduced in a recent application update, was repeatedly executed and led to high CPU and memory usage on the database servers. This caused a cascading effect, impacting various services.

Rollback Issues: During the incident, the decision to roll back to a previous application version was made. However, the rollback process itself caused brief service interruptions and was unsuccessful in fully resolving the problem.

Mitigation and Preventive Measures
Optimized Query: The slow query was immediately optimized, reducing its impact on the database servers. Additionally, ongoing monitoring and alerting have been implemented to detect similar issues in the future.

Improved Rollback Process: To prevent service interruptions during rollbacks, a rollback procedure was established, thoroughly tested, and documented. This ensures that if a similar situation arises, the rollback process can be executed more smoothly.

Code Review and Testing: Going forward, all code changes will undergo rigorous code review and testing to identify and address potential performance bottlenecks before deployment.

Enhanced Monitoring: We have enhanced our monitoring system to provide better visibility into database performance and the execution of critical queries.

Incident Response Training: All team members involved in incident response will receive additional training to improve their ability to diagnose and mitigate similar issues promptly.

Conclusion
The web stack outage on October 10, 2023, was a challenging incident that highlighted the need for improved monitoring, rollback procedures, and code review processes. By addressing the root causes and implementing preventive measures, we aim to strengthen our system's resilience and minimize the risk of similar outages in the future. We appreciate the patience and understanding of our users during this incident and are committed to maintaining the highest standards of service reliability
