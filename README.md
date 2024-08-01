# zuul-scs-jobs

Configuration of the SCS tenant at https://zuul.sovereignit.cloud

This repository accompanies
[zuul-config](https://github.com/SovereignCloudStack/zuul-config), and is
responsible for jobs and pipelines definitions of the `scs` tenant, while
`zuul-config` repository is responsible for the overall zuul installation.

Placement of projects into tenants is handled in `zuul-config` repository.


## Base job

``zuul.d/jobs.yaml``

## Pipelines configuration

- ``zuul.d/gh_pipelines.yaml``
- ``zuul.d/timer_pipelines.yaml``

## Projects

Projects without repositories and current project

``zuul.d/projects.yaml``

## Container jobs

``zuul.d/container-jobs.yaml``

## Secrets

Deprecated location for the secrets that are stored in git itself. New approach
is to keep secrets in Vault. This repository is enabled in accessing Vault and
getting all necessary secrets from there directly. In addition the base job
enables regular jobs to also get their corresponding token for accessing Vault
(while native implementation in Zuul providing JWT/OpenIDConnect token to the
jobs is not implemented). That does not mean any project gets access to the
Vault. Only projects having dedicated ApplicationRole in vault which are
registered in a special manner will be receive the token.

Please contact Zuul administrators to get further details.
