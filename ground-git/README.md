# Fiddling with git

Some experiments around git workflows using yaml.

## First experiment:

Find out what `$GITHUB_OUTPUT` and `$GITHUB_STEP_SUMMARY` is and how it behaves.

See `.github/workflows/experiment1.yml`

```yaml
name: Experiment1

  on:
    push:
      branches:
        - "main"
      paths:
        - ".github/workflows/experiment1.yaml"
```

This is a basic structure, it simply describes the Name of the workflow and when to trigger, in this case if changes to the file `./github/workflows/experiment1.yml` are pushed to main branch.

But we want to be able to manually trigger that workflow.

For that we simply need to add the keyword `workflow_dispatch:`, this allows you to trigger it manually.

Ok, basic setup is done, what next?
We need to tell it what to do, right?

In programming terms workflows are imperative and/or procedural.
So, they do one step after another (imperative) but the behaviour can change, due certain states (procedural).
For now lets keep it really simple and do all things I want to find out in a single step.

There is a keyword for it also called `jobs:`
Jobs are seperated in `steps:`
They have a huge variety of properties, but I dont want to go to deep into details here.
Please headover to [Github's workflow documentation](https://docs.github.com/en/actions/using-workflows).

For the rest, simply read the file mentioned in the beginning and try to 'reverse engineer', what is going on...

Cheers
