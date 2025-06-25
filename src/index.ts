import express from "express";
import { startServer } from "@modelcontextprotocol/sdk";
import { tool as filesystemTool } from "../AI-Policy-Navigator/servers/filesystem";
import { tool as memoryTool } from "../AI-Policy-Navigator/servers/memory";

const app = express();

startServer(app, {
  tools: [filesystemTool, memoryTool]
});

app.listen(3000, () => console.log("✅ MCP server running on http://localhost:3000"));
