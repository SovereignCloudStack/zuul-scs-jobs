Generate SBOM with Syft

**Role Variables**

.. zuul:rolevar:: generate_sbom_syft_source

   Source to generate SBOM for

.. zuul:rolevar:: generate_sbom_syft_format
   :default: cyclonedx-json

   Format of the SBOM report

.. zuul:rolevar:: generate_sbom_syft_path

   Path where to save the report
