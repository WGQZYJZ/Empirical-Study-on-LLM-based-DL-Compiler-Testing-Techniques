import torch

# Define an example function
def example_function(input_tensor):
    # Permute the last two dimensions
    permuted_tensor = input_tensor.permute(0, 2, 1)
    # Apply a linear transformation
    output_tensor = torch.nn.functional.linear(permuted_tensor, weight, bias)
    return output_tensor

# Create a PyTorch FX GraphModule for transformation
graph_module = torch.fx.symbolic_trace(example_function)
optimized_graph_module = permute_linear_fusion(graph_module)
