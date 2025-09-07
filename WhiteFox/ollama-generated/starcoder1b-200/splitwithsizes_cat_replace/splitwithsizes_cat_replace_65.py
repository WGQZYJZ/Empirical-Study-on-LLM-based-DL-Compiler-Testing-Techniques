# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor1, input_tensor2):
        # ... implementation of your optimized model


# Test
def test_optimized_model():
    m = Model()
    assert m.training is False  # The model is trained with the `torch.manual_seed` command within this method

    ... implementation of your optimized model


class Test:
    def test_optimized_model(self):
        m = Model()
        assert m.training is True  # The model is not trained with the `torch.manual_seed` command within this method


# Description of requirements
Your optimization should be applicable to any PyTorch model or any PyTorch class derived from `torch.nn.Module`. It does not need to be a specific PyTorch framework but it can use all basic operations such as arithmetic operations, array indexing, etc., provided by PyTorch like `torch.cat`, `torch.split` and so on.
