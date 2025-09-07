The model should contain the following pattern:
This pattern characterizes scenarios where `input_tensor` or `distribution` are not constant expressions. `lowmem_dropout(torch.rand_like(...))` will be replaced with `torch.rand_like(...)`. 

Note that if the `fallback_random` configuration is set, or if the model is running on a CPU device, the nodes invoking this function will not be replaced and thus will not trigger the `gm.graph.erase_node(node)
input_tensor = torch.randn((2, 2)) # Input to the model
output = m(input_tensor)
__model__ = gm.make_model("torch.nn.functional.lowmem_dropout", input_tensor=input_tensor, training=False)
output_0 = m.forward(input_tensor)
# The model is different from the previous one.
assert not __model__.is_identical(__model__) and (output - output_0).abs().max() > 1e-4


__model__ = gm.make_model("torch.nn.functional.lowmem_dropout", input_tensor=input_tensor, training=False)
output_0 = m.forward(input_tensor)
output_1 = __model__.forward(input_tensor)
assert not graph.is_identical(graph) and (output - output_0).abs().max() > 1e-4


output = m(input_tensor)
__model__ = gm.make_model("torch.nn.functional.lowmem_dropout", input_tensor=input_tensor, training=True)
output_0 = __model__.forward(input_tensor)
assert output == output_0


