# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where a model returns a non-leaf tensor. The optimizer would infer sink_cat_after_pointwise on such a pattern if it cannot find the correct target tensor for the model.

