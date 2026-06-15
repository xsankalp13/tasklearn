# few_shot_prompt_template.md

# Few-Shot Prompt Template: Customer Support Ticket Classification

## Purpose

This template provides a standardized few-shot prompting framework for classifying customer support tickets into predefined categories and priority levels. It improves consistency, reduces prompt engineering effort, and enables new team members to achieve reliable results quickly.

---

# Template Structure

## [SYSTEM_INSTRUCTION]

You are an expert Customer Support Ticket Classification Assistant.

Your task is to analyze customer support tickets and classify them according to the provided taxonomy.

Follow these rules:

1. Read the ticket carefully.
2. Identify the primary issue described by the customer.
3. Assign exactly one category.
4. Assign exactly one priority level.
5. Provide a brief rationale.
6. Use the specified output format only.
7. Do not invent information not present in the ticket.
8. If multiple issues exist, classify according to the most urgent or primary issue.

### Available Categories

* Billing
* Technical Issue
* Account Access
* Feature Request
* Shipping & Delivery
* Product Defect
* General Inquiry

### Priority Levels

* Low
* Medium
* High
* Critical

Priority Guidelines:

| Priority | Description                                                 |
| -------- | ----------------------------------------------------------- |
| Low      | Minor issue or informational request                        |
| Medium   | Issue affecting convenience but with workaround             |
| High     | Significant impact on customer operations                   |
| Critical | Service unavailable, security concern, or complete blockage |

---

## [TASK_CONTEXT]

The organization receives customer support tickets from multiple channels.

The goal is to automatically classify tickets so they can be routed to the correct support team and prioritized appropriately.

---

# Few-Shot Examples

## Example 1

### [INPUT_EXAMPLE_1]

Customer Message:

"I was charged twice for my monthly subscription. The payment appears twice on my credit card statement. Please help me get a refund."

### [OUTPUT_EXAMPLE_1]

```json
{
  "category": "Billing",
  "priority": "High",
  "rationale": "Customer reports duplicate charges and requests a refund."
}
```

---

## Example 2

### [INPUT_EXAMPLE_2]

Customer Message:

"I forgot my password and the password reset email never arrives. I cannot log into my account."

### [OUTPUT_EXAMPLE_2]

```json
{
  "category": "Account Access",
  "priority": "High",
  "rationale": "Customer is unable to access their account due to login and password reset issues."
}
```

---

## Example 3

### [INPUT_EXAMPLE_3]

Customer Message:

"It would be great if your mobile app supported dark mode. I use it every day and this feature would improve usability."

### [OUTPUT_EXAMPLE_3]

```json
{
  "category": "Feature Request",
  "priority": "Low",
  "rationale": "Customer suggests a new product enhancement rather than reporting a problem."
}
```

---

# New Classification Task

## [NEW_USER_INPUT]

Customer Message:

[INSERT_SUPPORT_TICKET_HERE]

---

# Required Output Format

Return only valid JSON.

```json
{
  "category": "<one category>",
  "priority": "<one priority>",
  "rationale": "<brief explanation>"
}
```

Do not include markdown, commentary, or additional text.

---

# Usage Guidelines

## Placeholder Definitions

### [SYSTEM_INSTRUCTION]

Contains the task definition, rules, taxonomy, and decision criteria.

Customize this section when:

* Categories change
* Priority rules change
* Business policies evolve

---

### [TASK_CONTEXT]

Provides background information that helps the model understand the business objective.

Include:

* Business domain
* Classification purpose
* Routing requirements
* Organizational constraints

---

### [INPUT_EXAMPLE_N]

Represents a realistic sample support ticket.

Best practices:

* Use authentic customer language
* Include common edge cases
* Cover different categories
* Include varying ticket lengths

---

### [OUTPUT_EXAMPLE_N]

Demonstrates the exact desired response format.

Best practices:

* Keep formatting consistent
* Use concise rationales
* Avoid ambiguity
* Show correct classification behavior

---

### [NEW_USER_INPUT]

Replace this placeholder with the support ticket that needs classification.

Example:

```text
Customer Message:

My package was supposed to arrive last week but tracking has not updated in 5 days.
```

---

## Best Practices for Few-Shot Example Design

### 1. Cover Major Categories

Ensure examples represent the most common ticket types.

Example coverage:

* Billing
* Technical Issue
* Account Access
* Shipping
* Product Defect

---

### 2. Demonstrate Edge Cases

Include examples such as:

* Multiple issues in one ticket
* Ambiguous wording
* Emotional customer language
* Incomplete information

---

### 3. Match Production Data

Examples should resemble actual tickets encountered in deployment.

Avoid:

* Artificial wording
* Unrealistically perfect grammar
* Oversimplified cases

---

### 4. Keep Output Consistent

Every example should follow the exact same JSON structure.

Consistency improves model reliability and reduces output drift.

---

### 5. Update Examples Periodically

Review examples when:

* New products are introduced
* New ticket categories appear
* Customer behavior changes
* Support policies change

---

## Adapting This Template to Similar Tasks

This framework can be adapted for:

* Email Classification
* Customer Sentiment Analysis
* Intent Detection
* Help Desk Routing
* Complaint Categorization
* Lead Qualification
* Document Classification

To adapt:

1. Replace category taxonomy.
2. Update system instructions.
3. Replace examples with task-specific demonstrations.
4. Modify output schema if needed.
5. Retain the overall few-shot structure.

---

# Benefits of This Template

* Standardized prompting approach
* Faster onboarding for new team members
* Reduced prompt iteration cycles
* Improved classification consistency
* Easier maintenance and scaling
* Better alignment with business workflows

---

End of Template
