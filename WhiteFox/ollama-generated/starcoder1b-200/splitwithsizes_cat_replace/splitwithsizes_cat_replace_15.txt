
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def is_valid_splitwithsizes_cat(self, inputs_list):
        if len(inputs_list) <= 1:
            return False

        first_split_tensor = inputs_list[0]
        # Check for at least one torch.split in the model.
        found_torch_split_count = sum([isinstance(input_tensor, torch.Tensor) for input_tensor in inputs_list])
        if not found_torch_split_count:
            return False

        # Check that all of these tensors are used in the concatenation operation.
        for i in range(len(inputs_list)):
            input_tensor = inputs_list[i]
            if not torch.all([torch.equal(input_tensor, first_split_tensor)]):
                break

        else:
            return True


# Inputs to the model
x1  = torch.randn(2, 3, 64, 64)
x2  = torch.randn(2, 8, 64, 64)
__output__  = Model().is_valid_splitwithsizes_cat([x1, x2])

