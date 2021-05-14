# Should I deploy today?

This action check the website shouldideploy.today and stops deployments if the site tells us not to do so. 

## Inputs

### `timezone`

**Required** The timezone which your product team is working in. Default `"UTC"`.

## Outputs

### `deploy`

If we should deploy yes or no.

## Example usage

uses: actions/shouldideploy-action@v1
with:
  timezone: 'UTC'