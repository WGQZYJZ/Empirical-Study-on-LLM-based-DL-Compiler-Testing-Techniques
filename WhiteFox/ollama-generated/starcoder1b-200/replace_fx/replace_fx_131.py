This pattern characterizes scenarios where the functions' call stacks are modified, and thus will trigger the `gm.graph.erase_node` method in our implementation of TorchScript.


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @torch.jit.script_method  # Mark function as a method using `torch.jit.script_method` decorator
    def dropout(input_tensor, p=0.5):
        ...
This pattern characterizes scenarios where the functions' call stacks are modified, and thus will trigger the `gm.graph.erase_node` method in our implementation of TorchScript.
