# System Design Interview Framework & Numbers Cheatsheet

Primary external reference: [System Design Primer](https://github.com/donnemartin/system-design-primer)

---

## 1. The 45-Minute System Design Delivery Template

### Step 1: Requirements & Scope (5 min)
- **Functional Requirements:** Top 3–4 core user flows (e.g., "Post tweet, view home timeline, follow user").
- **Non-Functional Requirements:**
  - Scale (DAU, peak QPS, read:write ratio).
  - Latency target (e.g., `< 200ms` p99 for reads).
  - Consistency vs. Availability trade-off (CAP theorem: strong consistency for payments/inventory vs. eventual consistency for social feeds).

### Step 2: Back-of-the-Envelope Estimations (5 min)
- $1\text{ day} = 86,400\text{ sec} \approx 10^5\text{ sec}$.
- $100\text{M DAU} \times 10\text{ requests/day} = 10^9\text{ req/day} \approx 10,000\text{ QPS}$ average ($\sim 20\text{k–}30\text{k}$ peak QPS).
- Storage: $\text{writes/day} \times \text{object size} \times 365 \times \text{years}$.

### Step 3: API & Data Model (5–10 min)
- Define core REST / gRPC / WebSocket endpoints (request params, response payload, pagination cursor).
- Choose storage engine:
  - **Relational (PostgreSQL/MySQL):** ACID transactions, structured joins, moderate write scale.
  - **Wide-Column / Key-Value (Cassandra/DynamoDB):** High write throughput, simple partition-key + sort-key access patterns.
  - **Cache (Redis/Memcached):** Sub-millisecond reads, rate limiting, leaderboards (`ZSET`), distributed locks.
  - **Blob Storage + CDN (S3 + CloudFront):** Media, images, videos, static assets.

### Step 4: High-Level Architecture (10 min)
- Draw the end-to-end read path and write path:
  `Client -> DNS/CDN -> Load Balancer / API Gateway -> Stateless Services -> Cache / Message Queue (Kafka/SQS) -> Database`.

### Step 5: Deep Dives & Bottlenecks (15 min)
Pick 2–3 critical challenges (proactively or guided by interviewer):
- **Partitioning / Sharding:** Consistent hashing, avoiding hot keys / celebrity problem (hybrid fan-out on write + fan-out on read).
- **Concurrency & Idempotency:** Idempotency keys, optimistic concurrency (`version` column), distributed locks, or sagas.
- **Fault Tolerance & Observability:** Replication (leader-follower, multi-leader), dead-letter queues, circuit breakers, exponential backoff + jitter.

---

## 2. Core Case Studies Checklist (Weeks 8–12)

- [ ] **URL Shortener (TinyURL)** — Base62 encoding, counter/Snowflake ID vs random collision, 301 vs 302 redirect caching.
- [ ] **Rate Limiter** — Token bucket, sliding window counter in Redis (`LUA` script for atomicity).
- [ ] **Distributed ID Generator** — 64-bit Twitter Snowflake (timestamp + datacenter + worker + sequence).
- [ ] **News Feed / Timeline** — Fan-out on write (push to followers' Redis lists) vs fan-out on read (pull for high-follower accounts).
- [ ] **Chat System (WhatsApp / Slack)** — WebSockets for real-time delivery, connection presence service, per-conversation sequence IDs in Cassandra.
- [ ] **Notification Service** — Multi-channel workers (APNs, FCM, Email, SMS), deduplication, retry queues, user preference cache.
- [ ] **Web Crawler** — URL frontier queue, politeness/rate-limiting per domain, SimHash content deduplication.
- [ ] **Ticketmaster / Flash Sale** — Seat reservation TTL holds in Redis + transactional DB booking, virtual waiting room queue.
