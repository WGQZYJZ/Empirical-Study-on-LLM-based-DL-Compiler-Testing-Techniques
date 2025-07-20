actual = torch.tensor([0.1, 0.2, 0.3])
expected = torch.tensor([0.1, 0.2, 0.3])
torch.testing.assert_close(actual, expected)
actual = torch.tensor([0.1, 0.2, 0.3])
expected = torch.tensor([0.1, 0.2, 0.4])
try:
    torch.testing.assert_close(actual, expected)
except AssertionError as e:
    print(e)
actual = torch.tensor([0.1, 0.2, 0.3])
expected = torch.tensor([0.1, 0.2, 0.4])