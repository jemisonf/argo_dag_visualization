# Argo DAG Visualizer

This is a CLI for creating graphviz visualizations of Argo Workflows DAG templates. It's written for Python 3.9 but is probably compatible with Python >=3.6 (f-string support required).

To run, first run

```
pip3 install -r requirements.txt
```

Then:

```
python3 ./dag_viz.py path_to_your_workflow.yaml template-name
```

You will get an output in your current working directory called `output.gv`. You can render it with

```
dot -Tpng -o graph.png output.gv
```

And then open `graph.png` to see the rendered graph.

