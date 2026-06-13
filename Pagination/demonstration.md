# Pagination Implementation Demonstration

## Start the Server

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 1. Default Pagination

### Request

```bash
curl "http://127.0.0.1:8000/api/orders"
```

### Browser URL

```text
http://127.0.0.1:8000/api/orders
```

### Expected Result

* Returns the first page of products
* Default page = 1
* Default limit = 10

Example response:

```json
{
  "page": 1,
  "limit": 10,
  "total": 100,
  "total_pages": 10,
  "data": [...]
}
```

---

## 2. Different Page Number

### Request

```bash
curl "http://127.0.0.1:8000/api/orders?page=2&limit=10"
```

### Browser URL

```text
http://127.0.0.1:8000/api/orders?page=2&limit=10
```

### Expected Result

* Returns products 11–20
* page = 2
* limit = 10

---

## 3. Different Page Size

### Request

```bash
curl "http://127.0.0.1:8000/api/orders?page=1&limit=5"
```

### Browser URL

```text
http://127.0.0.1:8000/api/orders?page=1&limit=5
```

### Expected Result

* Returns first 5 products
* total_pages becomes 20

Example response:

```json
{
  "page": 1,
  "limit": 5,
  "total": 100,
  "total_pages": 20,
  "data": [...]
}
```

---

## 4. Last Valid Page

### Request

```bash
curl "http://127.0.0.1:8000/api/orders?page=10&limit=10"
```

### Browser URL

```text
http://127.0.0.1:8000/api/orders?page=10&limit=10
```

### Expected Result

* Returns products 91–100
* Last valid page for a dataset of 100 products

---

## 5. Out-of-Range Page Request

### Request

```bash
curl "http://127.0.0.1:8000/api/orders?page=11&limit=10"
```

### Browser URL

```text
http://127.0.0.1:8000/api/orders?page=11&limit=10
```

### Expected Result

Since page 11 exceeds the available pages:

```json
{
  "page": 11,
  "limit": 10,
  "total": 100,
  "total_pages": 10,
  "data": []
}
```

---

## 6. Invalid Page Parameter

### Request

```bash
curl "http://127.0.0.1:8000/api/orders?page=0"
```

### Browser URL

```text
http://127.0.0.1:8000/api/orders?page=0
```

### Expected Result

FastAPI validation error:

```json
{
  "detail": [
    {
      "msg": "Input should be greater than or equal to 1"
    }
  ]
}
```

HTTP Status:

```text
422 Unprocessable Entity
```

---

## 7. Invalid Limit Parameter

### Request

```bash
curl "http://127.0.0.1:8000/api/orders?limit=0"
```

### Browser URL

```text
http://127.0.0.1:8000/api/orders?limit=0
```

### Expected Result

FastAPI validation error:

```json
{
  "detail": [
    {
      "msg": "Input should be greater than or equal to 1"
    }
  ]
}
```

HTTP Status:

```text
422 Unprocessable Entity
```

---

## Interactive API Testing

FastAPI automatically provides Swagger UI for testing.

Open:

```text
http://127.0.0.1:8000/docs
```

Use the **Try it out** button to test different values for:

* `page`
* `limit`

and observe the API responses directly in the browser.

---

## Summary

The pagination implementation supports:

* Configurable `page` query parameter
* Configurable `limit` query parameter
* Default pagination values
* Total record count
* Total page count
* Handling of out-of-range page requests
* Validation for invalid query parameters
* Interactive testing through Swagger UI
