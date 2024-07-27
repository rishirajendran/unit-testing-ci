pre_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-"
dom_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-"
top_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def is_prefix(prefix):
    if prefix[-1] == ' ':
        prefix = prefix[:-1]

    for letter in prefix:
        if letter not in pre_chars:
            return False

    if prefix[0] in ['_', '.', '-'] or prefix[-1] in ['_', '.', '-']:
        return False

    if "__" in prefix or ".." in prefix or "--" in prefix:
        return False

    return True


def is_domain(domain):
    if domain[0] == ' ':
        domain = domain[1:]

    for letter in domain:
        if letter not in dom_chars:
            return False

    if domain[0] == '-' or domain[-1] == '-':
        return False

    if "--" in domain:
        return False

    return True


def is_toplevel(toplevel):
    for letter in toplevel:
        if letter not in top_chars:
            return False

    if len(toplevel) < 2:
        return False

    return True


def is_email(email):
    email = email.strip()

    parts = email.split('@')

    if len(parts) != 2:
        return False

    other_parts = parts[1].split('.')

    if len(other_parts) != 2:
        return False

    prefix = parts[0]
    domain = other_parts[0]
    toplevel = other_parts[1]

    valid_prefix = is_prefix(prefix)
    valid_domain = is_domain(domain)
    valid_toplevel = is_toplevel(toplevel)

    if valid_prefix and valid_domain and valid_toplevel:
        return True

    return False


def main():
    email = "rishi.rajendran@duke.edu"
    print(is_email(email))


if __name__ == "__main__":
    main()
