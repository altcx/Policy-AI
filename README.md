# Policy-AI

This repository contains several Model Context Protocol (MCP) servers used for the Policy-AI project.

## Building the servers

Run the TypeScript compiler using the project configuration:

```bash
npx tsc -p AI-Policy-Navigator/tsconfig.json
```

This creates JavaScript output under `AI-Policy-Navigator/build`.

## Running the servers

### Filesystem server

```bash
node AI-Policy-Navigator/build/filesystem/index.js <allowed-directory>
```

### Memory server

```bash
node AI-Policy-Navigator/build/memory/index.js
```

Both servers use the MCP stdio transport and will print startup messages indicating they are running correctly.
