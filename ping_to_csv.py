#%%
import regex

def remove_header_and_footer(input_file: str) -> None:
    """
    Remove ping output header and footer
    """

    with open(input_file, 'r+') as f:
        
        lines = f.readlines()

        # Remove the header and last lines
        lines = lines[1:-4]

        f.seek(0)
        f.truncate()
        f.writelines(lines)

def ping_to_csv(input_file: str) -> None:
    
    with open(input_file, "r") as f:
        text = f.read()

    pattern = r"\[(\d+\.\d+)\] \d+ bytes from \d+\.\d+\.\d+\.\d+: icmp_seq=(\d+) ttl=\d+ time=(\d+\.?\d+) ms"
    header = "timestamp,icmp_seq,time_ms\n"

    def replacement(match=regex.Match[str]) -> str:
        return f"{match.group(1)},{match.group(2)},{match.group(3)}"

    output: str = header + regex.sub(pattern=pattern, repl=replacement, string=text)

    # Clear the file
    open(input_file, "w").close()

    with open(input_file, "w") as f:
        f.write(output)

#%%
input_file = "2024-09-01-1.csv"

remove_header_and_footer(input_file)
ping_to_csv(input_file)