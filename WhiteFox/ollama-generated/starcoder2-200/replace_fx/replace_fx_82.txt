
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor):
         return torch.nn.functional.dropout(input_tensor), torch.rand_like(input_tensor)

 # Initializing the model
 m = Model()
 
 # Inputs to the model
 x1  = torch.ones(2, 3)
 
# Few important hyperparameters that can be tuned:
max_depth: maximum depth (default: -1)

fallback_random: whether to fallback to randlike when there is no available dropout implementation on the CPU device (default: False).

max_op_count: maximum number of operations in the graph. This parameter does not consider tensor operations or replacements, which can be greater than  max_op_count. Also, this parameter does not include the root node. Hence, for example setting max_op_count to 10 will count only 5 operations. (default: -1).

max_replace_retry: maximum number of retries when trying to find a replacement that satisfies the requirements and is within the allowed memory limit. (default: 3)

max_size_retry: maximum number of retries when trying to generate a tensor with specific shape or random size (e.g., 10x2). This parameter should be used together with max_shape_retry in order for the generated tensor sizes to vary. Otherwise, the same size will always be generated. (default: 3)

max_tensor_retry: maximum number of retries when trying to generate a tensor that meets the specific size and dtype requirements. (default: 50).

max_replace_retry : maximum number of retries when trying to find a replacement that satisfies the requirements and is within the allowed memory limit. (default: 3)

max_shape_retry : maximum number of retries when trying to generate a tensor with specific shape or random size (e.g., 10x2). This parameter should be used together with max_size_retry in order for the generated tensor sizes to vary. Otherwise, the same size will always be generated. (default: 3)

max_tensor_retry : maximum number of retries when trying to generate a tensor that meets the specific size and dtype requirements. (default: 50).

max_value: maximum value a randomly generated tensor can take by default if fallback is enabled, and the input tensor is not fixed-size. If fallback randomization is disabled or a tensor is fixed-size but has values smaller than max_value, those values will be ignored. This parameter should only be used when `fallback_random` mode is enabled since otherwise, there would be no random numbers generated at all. (default: 10)

max_replacements : maximum number of replacements considered for each call to the algorithm (default: 3). For example if the max depth allowed is 5 then the algorithm will search 6 different possible models in the graph, one with the first 5 nodes and the last being a dropout. If there are two more ops that must be satisfied it will search combinations of size 7.

max_replacements_per_call : maximum number of replacements to consider per call (default: 1). This parameter is mainly used in case you want to control the number of replacements considered by the algorithm for each call. For example if we want 50 replacements then this parameter should be set to 4.

min_replacements : minimum number of replacements considered for each call (default: 1)

seed: seed for random number generators. (default: -1, which is randomly chosen every time.)

mem_limit: memory limit used in the algorithm. In case a model fails to be found within this limit then the algorithm will generate another one until either it succeeds or reaches the maximum retry count of max_replacements or max_replace_retry respectively. (default: -1)

no_bias : whether to exclude the bias term from a linear transformation (default: False).

opset : model version used in the algorithm for each call (default: 37). This parameter can be used to force a certain model version that will be considered when generating new models. It is mostly used together with min_replacements, max_replacements or both. In case it is -1 then it will not force any specific model version and generate models from the current version.

output: filename of the model to save. If this parameter has a value then the model is saved into the file as a pickle format. Otherwise if a path is specified in the input parameter then the model will be written there with the extension ".pt". Otherwise, the model is loaded without saving. 

op_name : list of allowed replacements. If it is set to 'drop_softmax' for example then only dropout and softmax can be replaced. Setting this parameter also requires the `opset` argument in order to limit the number of available operators. In case it has a value then the argument opset should not be used (default: 'all').

replace_bias : whether to replace bias with an equivalent replacement from `lowmem_ops` (default: False).

replacements_blacklist: list of operations that can't be replaced by any operation in `lowmem_ops`. For example, if `opset` is set to 37 and this parameter has the value ['adaptive.relu'] then a call to 'adaptive.relu' will not be considered during replacement. (default: None).

replacements_whitelist : list of operations that can't be replaced by any operation in `lowmem_ops`. For example, if `opset` is set to 37 and this parameter has the value ['adaptive.relu'] then a call to 'adaptive.relu' will not be considered during replacement. (default: None).

save_models : whether to save the generated models as pickles or not. It is mostly used when debugging the algorithm with limited retries or memory limit set in order for each call of the algorithm to generate a model. In case this parameter has value True then all the generated models are saved under a directory in the cwd named "saved_models". This parameter should be ignored in cases where the models must not be saved, which is also the default behavior when save_models=False (default: False).

verbose : whether to print some debug information. (default: True)

