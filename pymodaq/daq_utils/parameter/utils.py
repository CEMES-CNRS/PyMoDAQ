def get_widget_from_tree(parameter_tree, widget_instance):
    widgets = []
    for item in parameter_tree.listAllItems():
        if hasattr(item, 'widget'):
            if isinstance(item.widget, widget_instance):
                widgets.append(item.widget)
    return widgets


def get_param_path(param):
    """

    Parameters
    ----------
    param

    Returns
    -------

    """
    path = [param.name()]
    while param.parent() is not None:
        path.append(param.parent().name())
        param = param.parent()
    return path[::-1]


def iter_children(param,childlist=[]):
    """Get a list of parameters name under a given Parameter
        | Returns all childrens names.

        =============== ================================= ====================================
        **Parameters**   **Type**                           **Description**
        *param*          instance of pyqtgraph parameter    the root node to be coursed
        *childlist*      list                               the child list recetion structure
        =============== ================================= ====================================

        Returns
        -------
        childlist : parameter list
            The list of the children from the given node.


        Examples
        --------
        >>> import custom_parameter_tree as cpt
        >>> from pyqtgraph.parametertree import Parameter
        >>>     #Creating the example tree
        >>> settings=Parameter(name='settings')
        >>> child1=Parameter(name='child1', value=10)
        >>> child2=Parameter(name='child2',value=10,visible=True,type='group')
        >>> child2_1=Parameter(name='child2_1', value=10)
        >>> child2_2=Parameter(name='child2_2', value=10)
        >>> child2.addChildren([child2_1,child2_2])
        >>> settings.addChildren([child1,child2])
        >>>     #Get the child list from the param argument
        >>> childlist=cpt.iter_children(settings)
        >>>     #Verify the integrity of result
        >>> print(childlist)
        ['child1', 'child2', 'child2_1', 'child2_2']

    """
    for child in param.children():
        childlist.append(child.name())
        if 'group' in child.type():
            childlist.extend(iter_children(child,[]))
    return childlist


def iter_children_params(param,childlist=[]):
    """Get a list of parameters under a given Parameter

    """
    for child in param.children():
        childlist.append(child)
        if 'group' in child.type():
            childlist.extend(iter_children_params(child,[]))
    return childlist


def get_param_from_name(parent,name):
    """Get Parameter under parent whose name is name

    Parameters
    ----------
    parent: Parameter
    name: str

    Returns
    -------
    ch: Parameter

    """
    for child in parent.children():
        if child.name() == name:
            return child
        if 'group' in child.type():
            ch = get_param_from_name(child, name)
            if ch is not None:
                return ch