# Create the Clean Architecture structure for the Intelligent Recommendation System
# This script creates both the FastAPI Microservices-lite backend structure and Next.js frontend structure

$directories = @(
    "backend/app/api/v1/endpoints",
    "backend/app/core",
    "backend/app/db",
    "backend/app/models",
    "backend/app/schemas",
    "backend/app/services/recommendation",
    "backend/app/tests",
    "frontend/components/dashboard",
    "frontend/components/ui",
    "frontend/app/dashboard",
    "frontend/app/api",
    "frontend/lib/utils",
    "frontend/lib/hooks",
    "frontend/public/assets",
    "scripts",
    "docs"
)

foreach ($dir in $directories) {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    Write-Host "Created directory: $dir"
}

# Create placeholder init files for backend to ensure proper python package imports
$init_files = @(
    "backend/app/__init__.py",
    "backend/app/api/__init__.py",
    "backend/app/api/v1/__init__.py",
    "backend/app/services/__init__.py",
    "backend/app/services/recommendation/__init__.py"
)

foreach ($file in $init_files) {
    New-Item -ItemType File -Force -Path $file | Out-Null
}

Write-Host "`nClean Architecture folder structure generated successfully!"
Write-Host "Please see README.md for the next steps to run the Next.js and FastAPI environments."
