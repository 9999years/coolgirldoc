//! File tree traversal.

use std::path::Path;

use walkdir::DirEntry;
use walkdir::WalkDir;

fn is_python(entry: &DirEntry) -> bool {
    entry
        .file_name()
        .to_str()
        .map_or(false, |s| s.ends_with(".py"))
}

/// Iterate over Python files (files with names ending in `.py`) in a given
/// directory.
pub fn python_files<P: AsRef<Path>>(
    root: P,
) -> impl Iterator<Item = Result<DirEntry, walkdir::Error>> {
    WalkDir::new(root).into_iter().filter_entry(is_python)
}
