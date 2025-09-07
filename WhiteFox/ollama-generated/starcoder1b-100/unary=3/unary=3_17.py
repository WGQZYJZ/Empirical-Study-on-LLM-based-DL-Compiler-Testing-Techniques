The main reason is that `torch.mul()` should be applied to output tensor of `conv` when computing gradient of the loss with respect to `x1`. But this operation is not supported in Python and so this model will generate a model which cannot compute its gradient with respect to `x1`.

