import express from "express";
import { startServer } from "@modelcontextprotocol/sdk";
import { tools as filesystemTools } from "../AI-Policy-Navigator/servers/filesystem";
import { tools as memoryTools } from "../AI-Policy-Navigator/servers/memory";

const app = express();

startServer(app, {
  tools: [...filesystemTools, ...memoryTools]
});

app.listen(3000, () => console.log("✅ MCP server running on http://localhost:3000"));
