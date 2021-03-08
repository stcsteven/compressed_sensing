# visualize signal 
def visualize(plt, **kwargs):
    if 'figure_size' in kwargs:
        plt.figure(figsize=kwargs['figure_size'])
    if 'figure_title' in kwargs:
        plt.title(kwargs['figure_title'])

# Helper .class method 
def class_name(instance):
    return instance.__class__.__name__