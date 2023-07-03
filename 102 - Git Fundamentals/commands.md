# Git Commands

## Amending a commit message

```bash
git commit --amend -m 'New commit message'
```

## Amending a commit with additional code changes

```bash
git add .
git commit --amend --no-edit
```

## Git Branches

Creating and checkout out a new branch

```bash
git checkout -b new_branch
```

Committing this branch
    
```bash
git commit -m 'Created new branch'
```

Pushing this branch to the remote repository

```bash
git push origin new_branch
```

## Rebase multiple commits

```bash
git rebase -i HEAD~4
```
