# DSI Toolkit
## What is this?
I decided that it would be handy to have a centrally-accessible place to get at commonly used formulas and tools. This is that place. Mostly it is for my benefit, but if you feel that it would be useful for you to use it, please do!

## How do I install it?
Probably the easiest way to use it would be to clone (or fork/clone) the repo somewhere on your local machine. Then install using `pip install -e /path/to/repo`. If I were to put it in a `src` directory in my home folder, for example, I would do

```pip install -e ~/src/dsi-toolkit```

This would install the dsi-toolkit package in **editable** mode, which means that any changes to the package that are made (either via your own edits or by updating the repo) are automatically available next time you import the module

## How do I use it?
After installing, you can use the package anywhere you use python. All you have to do is `import toolkit`. You could also grab a specific module, such as `from toolkit import formulas` or grab a specific tool like `from toolkit.formulas import cosine_distance`

## How do I update it?
I you have cloned it from my repository, all you have to do is enter the directory and pull the changes down.

```
cd ~/src
git pull origin master
```
and you're all updated! The next time you `import toolkit` you'll be all set up with the latest master version. If you're feeling adventurous, you're more than welcome to grab the development version which is in the `devel` branch.