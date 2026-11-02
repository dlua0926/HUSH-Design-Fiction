# Collaboration workflow

1. Give each teammate access through GitHub repository settings. An AI uses its operator's authorised account/connector; it does not independently gain access from a link.
2. Give that AI the repository URL and ask it to read START_HERE.md, STATUS.md and AGENTS.md.
3. Pick an open task, name an owner and branch, and keep its scope clear.
4. Commit work with STATUS.md and WORK_LOG.md updates. Open a PR for another teammate to review when it changes rules, narrative or final materials.
5. Before merging, check current main to prevent conflicting story rules, duplicate tasks and stale assets.

Recommended branches: narrative/<topic>, prototype/<topic>, physical/<topic>, advertisement/<topic>, docs/<topic>.

Use GitHub Issues for task status and questions. Use source files and progress docs as durable context; don't rely on a model recalling another chat. The repository is public at setup; invitation/edit permissions and each AI connector's repository selection are controlled by the account owners.

Progress is updated during actual work sessions. No unattended monitoring, automatic ingestion of every teammate chat, or scheduled sync is configured.

The HTML app is buildless. Open prototype/index.html locally or serve the prototype directory. Fonts may load from Google Fonts; system fallbacks are supplied. No search text is sent to a search engine. Network and checkout are simulations.
