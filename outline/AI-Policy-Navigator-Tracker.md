# AI Policy Navigator: Project Tracker

## Overview
This document tracks the development of the AI Policy Navigator prototype—a local-first Retrieval-Augmented Generation (RAG) system for answering questions about local government policies and legal documents.

---

## Milestones & Tasks

### 1. Project Setup
- [x] Define project structure and core components
- [x] Set up Python virtual environment and install dependencies
- [x] Create initial folder structure

### 2. PDF Ingestion
- [x] Implement script to extract text from digital PDFs
- [x] Add OCR support for scanned PDFs
- [x] Save extracted text for further processing

### 3. Embedding & Vector Store (MCP Integration)
- [x] Chunk extracted text
- [ ] Generate embeddings for each chunk using MCP server
- [ ] Store embeddings in a local vector database

### 4. Query & Retrieval (MCP Integration)
- [ ] Implement similarity search over vector store
- [ ] Use MCP server to generate answers from LLM using retrieved context

### 5. User Interface
- [ ] Build simple CLI or web UI for demo

---

## Notes & Decisions
- PowerShell is the default shell for all CLI instructions
- All code and scripts should run locally (no cloud dependencies unless using a remote MCP server)
- **MCP (Model Context Protocol) will be used for both embedding generation and LLM inference.**
- LM Studio or another MCP-compatible server will be used locally for maximum privacy and flexibility.

---

## Next Steps
- Start and configure the MCP server (e.g., LM Studio)
- Update embedding and retrieval scripts to use MCP endpoints
