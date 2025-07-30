#!/bin/bash

# Helper script for making commits with Commitizen
# Usage: ./scripts/commit.sh

echo "🚀 Using Commitizen for conventional commits..."
echo ""

# Check if there are staged changes
if git diff --cached --quiet; then
    echo "❌ No staged changes found!"
    echo "   Please stage your changes first with: git add ."
    exit 1
fi

# Run Commitizen
cz commit

echo ""
echo "✅ Commit created successfully!"
echo "   Use 'git push' to push your changes." 