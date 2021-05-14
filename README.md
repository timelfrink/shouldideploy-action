# Should I deploy today?

This action checks the website [shouldideploy.today](https://shouldideploy.today/) and stops deployments if the site tells us not to do so. 

## Inputs

### `timezone`

**Required** The timezone which your product team is working in. Default `"UTC"`.

## Force deploy
If you want to force the build and skip the check you can add `force deploy` to your commit message. 

## Example usage

```
uses: actions/shouldideploy-action@v1
with:
  timezone: 'UTC'
```
