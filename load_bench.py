from datasets import load_dataset
import subprocess

def dowmload_repo(repo, path):
    url = f"https://github.com/{repo}.git"
    #!git clone $url $path
    print(f"Cloning {url} to {path}")
    subprocess.run(["git", "clone", url, path])

if __name__ == "__main__":
    dataset = load_dataset("princeton-nlp/SWE-bench")
    print(dataset["dev"])

    print(dataset["dev"][0]["repo"])
    print(dataset["dev"][0]["problem_statement"])

    dowmload_repo(dataset["dev"][0]["repo"], "repo")
