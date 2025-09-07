
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        t1 = torch.cat([x1, x2], dim=0)  # Concatenate the three input tensors along the third dimension
        t2 = self.split_tensors(t1, [1, 1, 3], dim=2)  # Split the first and second input tensor along a second dimension
        return self.concatenated_tensor(t2)
 
    def split_tensors(self, input_tensor, split_sizes, dim):  # Return tensors based on sizes given in `split_sizes` for `dim`.
        if not torch.any([s > 0 for s in split_sizes]):
            raise ValueError('The sizes of each split must be positive.')
        if not len(input_tensor.shape) == 2:
            raise ValueError('All inputs to the model must have a single dimension.')
        if input_tensor.ndim != dim + 1 or torch.any([s > input_tensor.size()[dim] for s in split_sizes]):
            raise ValueError('Some tensors are used incorrectly. Please check your implementation and fix it!')
        return [input_tensor[:, :, idx * s : (idx+1) * s, :]
                for idx, s in enumerate(split_sizes)]
 
    def concatenated_tensor(self, split_tensors):  # Return the concatenation of `split_tensors`.
        return torch.cat([x for x in zip(*split_tensors)], dim=dim)


# Initializing the model
m = Model()

