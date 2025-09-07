import express from 'express'

const app = express()

app.get('/health', (_req, res) => {
  res.json({ ok: true })
})

const port = Number(process.env.PORT || 3001)

if (process.env.NODE_ENV !== 'test') {
  app.listen(port, () => {
    // eslint-disable-next-line no-console
    console.log(`api listening on :${port}`)
  })
}

export default app

