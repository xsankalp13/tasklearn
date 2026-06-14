# AI Prompt Library

A curated collection of reusable, production-ready AI prompts designed to support high-impact marketing workflows across a SaaS organization.

This library serves as a centralized source of truth for prompt engineering, helping marketers, content creators, growth teams, sales teams, and product marketers generate consistent, high-quality outputs using AI.

---

## Purpose

The goal of this library is to:

- Standardize AI-assisted content creation workflows
- Improve content quality and consistency
- Reduce prompt-writing overhead for team members
- Accelerate content production across channels
- Capture and share prompt engineering best practices
- Create reusable assets that can evolve over time

Each prompt is stored as structured JSON metadata to support future integration with AI tools, prompt management systems, internal platforms, or agent workflows.

---

## Library Structure

```text
AI_Prompt_Library/
└── content_categories/
    ├── blog_and_seo/
    ├── social_media_content/
    ├── email_marketing/
    ├── paid_advertising_copy/
    └── sales_enablement_and_outbound_content/
```

Each category contains prompts related to a specific marketing workflow.

Example:

```text
social_media_content/
├── social_media_content_prompt_1.json
├── social_media_content_prompt_2.json
└── social_media_content_prompt_3.json
```

---

## Prompt Schema

Every prompt follows a consistent metadata structure:

```json
{
  "title": "Prompt Name",
  "category": ["Category"],
  "persona": "Target User",
  "goal": "Desired Outcome",
  "prompt": "Full Prompt Template",
  "variables": [],
  "best_practices": [],
  "date_created": "",
  "date_updated": "",
  "author": "system"
}
```

### Key Fields

| Field | Description |
|---------|-------------|
| title | Human-readable prompt name |
| category | Associated content category |
| persona | Intended user role |
| goal | Business objective |
| prompt | Full AI instruction template |
| variables | Dynamic user inputs |
| best_practices | Usage recommendations |
| date_created | Initial creation timestamp |
| date_updated | Last modification timestamp |
| author | Prompt creator or owner |

---

## How to Use

### 1. Select the Appropriate Prompt

Choose a prompt based on the workflow:

| Need | Category |
|--------|----------|
| SEO Research | Blog & SEO |
| Blog Writing | Blog & SEO |
| LinkedIn Content | Social Media |
| Newsletter Creation | Email Marketing |
| Ad Copy | Paid Advertising |
| Cold Outreach | Sales Enablement |

---

### 2. Populate Variables

Replace placeholder variables before execution.

Example:

```text
{target_audience}
{product_description}
{offer}
{campaign_objective}
```

with:

```text
Marketing Managers at B2B SaaS companies

AI-powered lead generation platform

14-day free trial

Increase demo bookings
```

---

### 3. Review Outputs

AI-generated content should always undergo:

- Fact checking
- Brand review
- Compliance review (if applicable)
- SEO review (for content assets)
- Final human editing

Prompts are designed to accelerate creation—not replace editorial judgment.

---

## Prompt Design Principles

All prompts in this library should:

### Be Role-Based

Clearly define who the AI is acting as.

Example:

```text
Role:
You are a senior SaaS content strategist.
```

---

### Be Goal-Oriented

Specify the business outcome.

Example:

```text
Objective:
Generate a high-converting LinkedIn post.
```

---

### Include Constraints

Guide output quality and reduce hallucinations.

Example:

```text
Constraints:
- Avoid fluff
- Focus on customer outcomes
- Use concise language
```

---

### Use Structured Outputs

Outputs should be predictable and reusable.

Example:

```text
Output Format:
1. Hook
2. Main Insight
3. CTA
```

---

## Modifying Existing Prompts

When updating prompts:

### Do

✅ Improve clarity

✅ Add stronger constraints

✅ Enhance output structure

✅ Add missing variables

✅ Update best practices

✅ Version meaningful changes

---

### Don't

❌ Remove metadata fields

❌ Add company-specific assumptions

❌ Hardcode temporary campaigns

❌ Make prompts overly verbose

❌ Change output formats without justification

---

## Adding New Prompts

Before creating a new prompt:

1. Verify that a similar prompt does not already exist.
2. Ensure the prompt solves a repeatable workflow.
3. Use the standard metadata schema.
4. Include meaningful variables.
5. Add usage best practices.
6. Assign the correct category.

Recommended naming convention:

```text
<category>_prompt_<number>.json
```

Example:

```text
email_marketing_prompt_4.json
```

---

## Versioning Guidelines

Whenever a prompt is modified:

```json
{
  "date_updated": "2026-06-15T00:00:00Z"
}
```

Major improvements should be documented in commit messages or changelogs.

Example:

```text
feat: improve SEO brief generator semantic keyword analysis

fix: refine outbound email prompt constraints

refactor: standardize CTA generation outputs
```

---

## Future Expansion Areas

Potential categories to add:

- Product Marketing
- Customer Marketing
- Video & Webinar Content
- Marketing Operations
- Customer Success Content
- Community Marketing
- PR & Communications
- ABM Campaigns
- Event Marketing
- AI Agent Workflows

---

## Guiding Principle

This library should prioritize **reusability, consistency, and business impact** over one-off prompt experimentation.

If a prompt cannot be reused by multiple team members across multiple campaigns, it likely does not belong in the library.