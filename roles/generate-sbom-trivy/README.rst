Generate SBOM with Trivy

**Role Variables**

.. zuul:rolevar:: generate_sbom_trivy_source

   Source to generate SBOM for

.. zuul:rolevar:: generate_sbom_trivy_format
   :default: cyclonedx

   Format of the SBOM report

.. zuul:rolevar:: generate_sbom_trivy_path

   Path where to save the report
