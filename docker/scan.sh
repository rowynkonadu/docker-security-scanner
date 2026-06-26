    #!/bin/bash
    IMAGE=$1
    echo "Scanning $IMAGE..."
    docker run --rm -v ${PWD}:/out aquasec/trivy image --format json -o /out/trivy.json $IMAGE
    python src/generate_report.py
    echo "Done. Open report.html"