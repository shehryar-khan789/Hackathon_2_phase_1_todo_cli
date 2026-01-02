---
description: "Task list for Todo In-Memory Python Console App"
---

# Tasks: Todo In-Memory Python Console App (Phase I)

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 [P] Initialize Python project with proper directory structure (src/, tests/)
- [X] T003 [P] Create directory structure: src/models/, src/services/, src/cli/, src/lib/, tests/unit/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T004 Create TodoItem model in src/models/todo.py with id, description, status, created_at fields
- [X] T005 [P] Implement TodoService in src/services/todo_service.py with in-memory storage
- [X] T006 [P] Create constants file in src/lib/constants.py for application constants
- [X] T007 Implement basic CLI structure in src/cli/todo_cli.py using argparse
- [X] T008 Add type hints to all foundational components

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo Item (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items to their in-memory todo list via CLI command

**Independent Test**: Can be fully tested by running the add command with a todo description and verifying the item appears in the list.

### Implementation for User Story 1

- [X] T009 [P] [US1] Implement TodoItem constructor with validation in src/models/todo.py
- [X] T010 [P] [US1] Add add_todo method to TodoService in src/services/todo_service.py
- [X] T011 [US1] Add CLI command for adding todos in src/cli/todo_cli.py
- [X] T012 [US1] Implement validation for empty todo descriptions
- [X] T013 [US1] Add unique ID assignment for new todos
- [X] T014 [US1] Add auto-timestamp for created_at field
- [X] T015 [US1] Test adding todo functionality manually

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todo Items (Priority: P2)

**Goal**: Enable users to view all their todo items with their current status via CLI command

**Independent Test**: Can be fully tested by adding some todo items and then running the view command to see the list.

### Implementation for User Story 2

- [X] T016 [P] [US2] Add get_all_todos method to TodoService in src/services/todo_service.py
- [X] T017 [US2] Add CLI command for viewing todos in src/cli/todo_cli.py (list/view)
- [X] T018 [US2] Implement human-readable output format for todo list
- [X] T019 [US2] Handle case when no todos exist in the list
- [X] T020 [US2] Display ID, description, and status for each todo
- [X] T021 [US2] Test viewing todo functionality manually

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Todo Complete (Priority: P3)

**Goal**: Enable users to mark specific todo items as complete after finishing the task via CLI command

**Independent Test**: Can be fully tested by adding a todo item, then running the complete command on it, and verifying its status changes to complete.

### Implementation for User Story 3

- [X] T022 [P] [US3] Add mark_complete method to TodoService in src/services/todo_service.py
- [X] T023 [US3] Add CLI command for marking todos complete in src/cli/todo_cli.py
- [X] T024 [US3] Implement status transition validation (pending → complete only)
- [X] T025 [US3] Support both "complete <id>" and "mark <id> complete" commands
- [X] T026 [US3] Add error handling for non-existent todo IDs
- [X] T027 [US3] Test marking todo complete functionality manually

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Additional Features - Delete and Update (Priority: P4)

**Goal**: Implement remaining core features: delete and update todo items

**Independent Test**: Can be tested by performing delete and update operations and verifying they work correctly.

### Implementation for Delete Feature

- [X] T028 [P] [US4] Add delete_todo method to TodoService in src/services/todo_service.py
- [X] T029 [US4] Add CLI command for deleting todos in src/cli/todo_cli.py
- [X] T030 [US4] Add error handling for non-existent todo IDs during delete

### Implementation for Update Feature

- [X] T031 [P] [US4] Add update_todo method to TodoService in src/services/todo_service.py
- [X] T032 [US4] Add CLI command for updating todos in src/cli/todo_cli.py
- [X] T033 [US4] Add validation for empty new descriptions during update
- [X] T034 [US4] Add error handling for non-existent todo IDs during update
- [X] T035 [US4] Test delete and update functionality manually

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T036 [P] Add comprehensive error handling and user-friendly messages
- [X] T037 Add input validation across all CLI commands
- [X] T0038 [P] Add proper output formatting to stdout/stderr as specified
- [X] T039 Add documentation comments to all functions
- [X] T040 Run manual tests to verify all 5 basic features work
- [X] T041 Verify application meets performance goals (under 1 second response)
- [X] T042 Verify all requirements from spec are implemented

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Depends on TodoItem model and service layer

### Within Each User Story

- Models before services
- Services before CLI commands
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence