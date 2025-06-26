import express from "express";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { tools as filesystemTools } from "../AI-Policy-Navigator/servers/filesystem/index.js";
import { tools as memoryTools } from "../AI-Policy-Navigator/servers/memory/index.js";
import { tools as braveSearchTools } from "../AI-Policy-Navigator/servers/brave-search/index.js";
import { tools as puppeteerTools } from "../AI-Policy-Navigator/servers/puppeteer/index.js";
import { tools as sequentialThinkingTools } from "../AI-Policy-Navigator/servers/sequentialthinking/index.js";
const app = express();
// Aggregate all tools
const allTools = [
    ...filesystemTools,
    ...memoryTools,
    ...braveSearchTools,
    ...puppeteerTools,
    ...sequentialThinkingTools,
];
// Example server instantiation (adjust as needed for your use case)
const server = new Server({
    name: "PolicyAI Server",
    version: "1.0.0",
}, {
    // Add any server options here
    capabilities: {},
    // Optionally, you can add tools here if the SDK supports it
    // tools: allTools
});
app.listen(3000, () => console.log("✅ MCP server running on http://localhost:3000"));
